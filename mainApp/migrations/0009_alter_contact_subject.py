# Generated by Django 4.0.2 on 2022-03-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
