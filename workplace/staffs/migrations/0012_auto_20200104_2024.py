# Generated by Django 2.0.5 on 2020-01-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0011_administration_occupation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administration',
        ),
        migrations.AddField(
            model_name='staffer',
            name='specialization',
            field=models.CharField(default='', max_length=50),
        ),
    ]
