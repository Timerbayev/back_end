# Generated by Django 2.0.5 on 2020-01-01 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0005_auto_20181110_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffer',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
