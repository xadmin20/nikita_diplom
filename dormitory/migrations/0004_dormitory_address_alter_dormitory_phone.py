# Generated by Django 5.0.6 on 2024-05-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0003_alter_pointshistory_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitory',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='dormitory',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон'),
        ),
    ]