# Generated by Django 4.0.2 on 2022-03-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
