# Generated by Django 4.0.4 on 2022-09-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_outpass_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outpassform',
            name='proofletter',
            field=models.FileField(upload_to='proofphotos'),
        ),
        migrations.AlterField(
            model_name='outpassformaccepted',
            name='proofletter',
            field=models.FileField(upload_to='proofphotos'),
        ),
    ]
