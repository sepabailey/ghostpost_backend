# Generated by Django 3.0.7 on 2020-06-25 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='results',
        ),
    ]
