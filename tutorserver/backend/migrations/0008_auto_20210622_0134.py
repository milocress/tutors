# Generated by Django 3.1.7 on 2021-06-22 01:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0007_auto_20210427_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='tutor',
            options={'ordering': ['user']},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('user',)},
        ),
        migrations.AlterUniqueTogether(
            name='tutor',
            unique_together={('user',)},
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='name',
        ),
    ]