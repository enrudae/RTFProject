# Generated by Django 4.2 on 2023-05-29 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_education_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='education_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.educationform'),
        ),
        migrations.AlterField(
            model_name='student',
            name='education_stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='education_stage', to='students.educationstage'),
        ),
    ]