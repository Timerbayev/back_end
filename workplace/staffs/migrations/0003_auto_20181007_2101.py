# Generated by Django 2.0.5 on 2018-10-07 18:01

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0002_auto_20181006_2053'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='staffer',
            managers=[
                ('staff', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='staffer',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='staffer',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='staffer',
            name='mobile',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
