# Generated by Django 5.0.6 on 2024-05-10 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='student',
        ),
    ]
