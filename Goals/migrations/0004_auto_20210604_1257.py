# Generated by Django 3.2.3 on 2021-06-04 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Goals', '0003_auto_20210604_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='Date_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Date_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Date_start',
            field=models.DateTimeField(),
        ),
    ]
