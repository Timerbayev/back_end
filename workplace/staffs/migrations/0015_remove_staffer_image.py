# Generated by Django 2.0.5 on 2020-01-17 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0014_auto_20200115_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffer',
            name='image',
        ),
    ]
