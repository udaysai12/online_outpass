# Generated by Django 4.0.4 on 2022-09-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=64)),
                ('adminpassword', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Outpassform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=64)),
                ('sklmid', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('studentph', models.CharField(max_length=10)),
                ('parentname', models.CharField(max_length=64)),
                ('parentph', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=64)),
                ('rclass', models.CharField(max_length=64)),
                ('outdate', models.DateField()),
                ('reportingdate', models.DateField()),
                ('reason', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=254)),
                ('proofletter', models.FileField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Outpassformaccepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=64)),
                ('sklmid', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('studentph', models.CharField(max_length=10)),
                ('parentname', models.CharField(max_length=64)),
                ('parentph', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=64)),
                ('rclass', models.CharField(max_length=64)),
                ('outdate', models.DateField()),
                ('reportingdate', models.DateField()),
                ('reason', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=254)),
                ('proofletter', models.FileField(upload_to='photos')),
            ],
        ),
    ]
