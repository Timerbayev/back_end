# Generated by Django 2.0.5 on 2018-10-07 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0003_auto_20181007_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffer',
            name='birthday',
        ),
    ]
