from django.forms import ModelForm
from .models import Student, Specialization, EducationForm, EducationStage, FinancingForm, Citizenship
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    pass


class CustomSelectWidget(forms.Select):
    template_name = 'students/custom_select_widget.html'  # Путь к файлу шаблона виджета


class StudentCreationForm(ModelForm):
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), to_field_name='title',
                                            required=False)
    education_form = forms.ModelChoiceField(queryset=EducationForm.objects.all(), to_field_name='title', required=False)
    education_stage = forms.ModelChoiceField(queryset=EducationStage.objects.all(), to_field_name='title',
                                             required=False)
    financing_form = forms.ModelChoiceField(queryset=FinancingForm.objects.all(), to_field_name='title', required=False)
    citizenship = forms.ModelChoiceField(queryset=Citizenship.objects.all(), to_field_name='title', required=False)

    class Meta:
        model = Student
        exclude = ['is_deleted']


class FilterForm(forms.Form):
    specialization = forms.ModelMultipleChoiceField(queryset=Specialization.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple, to_field_name='title',
                                                    required=False)
    education_form = forms.ModelMultipleChoiceField(queryset=EducationForm.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple, to_field_name='title',
                                                    required=False)
    education_stage = forms.ModelMultipleChoiceField(queryset=EducationStage.objects.all(),
                                                     widget=forms.CheckboxSelectMultiple, to_field_name='title',
                                                     required=False)
