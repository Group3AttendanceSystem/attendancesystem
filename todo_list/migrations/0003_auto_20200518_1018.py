# Generated by Django 3.0.6 on 2020-05-18 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20200518_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
