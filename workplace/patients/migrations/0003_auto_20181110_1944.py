# Generated by Django 2.0.5 on 2018-11-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20181006_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='birthday',
            field=models.DateField(blank=True),
        ),
    ]