# Generated by Django 3.1.7 on 2021-03-29 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of student')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of subject')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of tutor')),
                ('specialties', models.ManyToManyField(related_name='tutors', to='backend.Subject')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='TutorSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_sessions', to='backend.student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_sessions', to='backend.tutor')),
            ],
        ),
    ]