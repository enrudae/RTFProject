from django.contrib import admin
from .models import FinancingForm, EducationStage, EducationForm, Specialization, Citizenship, Student, \
    StudentParticipation, Achievements

admin.site.register(FinancingForm)
admin.site.register(EducationStage)
admin.site.register(EducationForm)
admin.site.register(Specialization)
admin.site.register(Citizenship)
admin.site.register(Student)
admin.site.register(StudentParticipation)
admin.site.register(Achievements)
