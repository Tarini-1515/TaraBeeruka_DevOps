# Generated by Django 3.2.5 on 2021-07-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(error_messages={'required': 'You cannot leave name field empty'}, help_text='Make sure to enter your ', max_length=70),
        ),
    ]
