from django.db import models


class FinancingForm(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Форма финансирования"
        verbose_name_plural = "Формы финансирования"

    def __str__(self):
        return self.title


class EducationStage(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Ступень образования"
        verbose_name_plural = "Ступень образования"

    def __str__(self):
        return self.title


class EducationForm(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Форма обучения"
        verbose_name_plural = "Формы обучения"

    def __str__(self):
        return self.title


class Specialization(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.title


class Citizenship(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Гражданство"
        verbose_name_plural = "Гражданства"

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    start_education_date = models.IntegerField(blank=True, null=True)
    end_education_date = models.IntegerField(blank=True, null=True)
    living_place = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    group = models.CharField(max_length=255, blank=True, null=True)

    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    education_form = models.ForeignKey(EducationForm, on_delete=models.SET_NULL, blank=True, null=True)
    education_stage = models.ForeignKey(EducationStage, related_name='education_stage', on_delete=models.SET_NULL, blank=True, null=True)
    financing_form = models.ForeignKey(FinancingForm, on_delete=models.SET_NULL, blank=True, null=True)
    citizenship = models.ForeignKey(Citizenship, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ['first_name', '-start_education_date']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class StudentParticipation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    student = models.ForeignKey(Student, verbose_name="Студент", related_name='student_participation', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Студенческие активности"
        verbose_name_plural = "Студенческие активности"

    def __str__(self):
        return self.title


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    student = models.ForeignKey(Student, verbose_name="Студент", related_name='achievements', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Достижения"
        verbose_name_plural = "Достижение"

    def __str__(self):
        return self.title
