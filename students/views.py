from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Student
from students.forms import RegisterForm


@login_required
def profile_view(request):
    return render(request, 'students/profile.html')


@login_required
def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/all_students.html', {'students': students})


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('students:profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
