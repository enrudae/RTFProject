from django.forms import ModelForm
from .models import Student, Specialization, EducationForm, EducationStage, FinancingForm, Citizenship
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    pass


class CustomSelectWidget(forms.Select):
    template_name = 'students/custom_select_widget.html'  # Путь к файлу шаблона виджета


class StudentCreationForm(ModelForm):
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), to_field_name='title')
    education_form = forms.ModelChoiceField(queryset=EducationForm.objects.all(), to_field_name='title')
    education_stage = forms.ModelChoiceField(queryset=EducationStage.objects.all(), to_field_name='title')
    financing_form = forms.ModelChoiceField(queryset=FinancingForm.objects.all(), to_field_name='title')
    citizenship = forms.ModelChoiceField(queryset=Citizenship.objects.all(), to_field_name='title')

    class Meta:
        model = Student
        exclude = ['is_deleted']