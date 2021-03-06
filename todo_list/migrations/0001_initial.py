# Generated by Django 3.0.6 on 2020-05-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eventList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('event', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
