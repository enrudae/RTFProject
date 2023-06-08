from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Student, StudentParticipation, Specialization, EducationStage, EducationForm
from students.forms import StudentCreationForm, RegisterForm, FilterForm
from django.core.paginator import Paginator
from django.db.models import Q


@login_required
def all_students(request):
    students = Student.objects.all()
    form = FilterForm(request.GET)
    selected_filters = []

    if form.is_valid():
        specializations = form.cleaned_data['specialization']
        education_form = form.cleaned_data['education_form']
        education_stage = form.cleaned_data['education_stage']

        if specializations:
            students = students.filter(specialization__in=specializations)
            selected_filters += list(specializations)

        if education_form:
            students = students.filter(education_form__in=education_form)
            selected_filters += list(education_form)

        if education_stage:
            students = students.filter(education_stage__in=education_stage)
            selected_filters += list(education_stage)

    query = request.GET.get('query')

    if query:
        students = students.filter(
            Q(first_name__iregex=query) |
            Q(last_name__iregex=query) |
            Q(patronymic__iregex=query) |
            Q(end_education_date__iregex=query) |
            Q(group__iregex=query) |
            Q(specialization__title__iregex=query)
        )

    sort_option = request.GET.get('sort_option')

    if sort_option == 'inc_year':
        students = students.order_by('end_education_date')
    elif sort_option == 'dec_year':
        students = students.order_by('-end_education_date')
    elif sort_option == 'inc_last_name':
        students = students.order_by('last_name')

    paginator = Paginator(students, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 'sort_option': sort_option, 'query': query, 'form': form, 'selected_filters': selected_filters
    }

    return render(request, 'students/students_table.html', context)


@login_required
def student(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, 'students/student_profile.html', {'student': student})


@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            return redirect('students:all_students')
    else:
        form = StudentCreationForm()

    return render(request, 'students/student_create.html', {'form': form})


@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    education_stages = EducationStage.objects.all()

    if request.method == 'POST':
        form = StudentCreationForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('students:all_students')
    else:
        form = StudentCreationForm(instance=student)

    return render(request, 'students/student_edit.html',
                  {'form': form, 'student': student, 'education_stages': education_stages})


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('students:profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
