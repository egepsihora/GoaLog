# Generated by Django 3.2.3 on 2021-06-04 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Goals', '0002_auto_20210604_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='Title',
        ),
        migrations.AddField(
            model_name='group',
            name='Help_text',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Date_create',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Date_start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='goal',
            name='Title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]