# Generated by Django 3.0.6 on 2020-09-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_student_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyAdvisor',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]