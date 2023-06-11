from django.forms import ModelForm
from .models import Student, Specialization, EducationForm, EducationStage, FinancingForm, Citizenship
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomSelectWidget(forms.Select):
    template_name = 'students/custom_select_widget.html'


class StudentCreationForm(ModelForm):
    specialization = forms.CharField(required=False)
    education_form = forms.CharField(required=False)
    education_stage = forms.CharField(required=False)
    financing_form = forms.CharField(required=False)
    citizenship = forms.CharField(required=False)

    def clean_field(self, field_name, model_class):
        value = self.cleaned_data[field_name]

        if value:
            obj = model_class.objects.filter(title=value).first()
            if not obj:
                obj = model_class.objects.create(title=value)

            return obj
        return None

    def clean_specialization(self):
        return self.clean_field('specialization', Specialization)

    def clean_education_form(self):
        return self.clean_field('education_form', EducationForm)

    def clean_education_stage(self):
        return self.clean_field('education_stage', EducationStage)

    def clean_financing_form(self):
        return self.clean_field('financing_form', FinancingForm)

    def clean_citizenship(self):
        return self.clean_field('citizenship', Citizenship)

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
