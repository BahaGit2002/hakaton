# Generated by Django 5.1.6 on 2025-02-22 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_accommodation_organised_course_has_grade_requirement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grade_system',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='qualitative_grade',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
