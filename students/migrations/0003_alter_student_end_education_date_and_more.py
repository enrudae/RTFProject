# Generated by Django 4.2 on 2023-05-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='end_education_date',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_education_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]