# Generated by Django 2.0.5 on 2018-11-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0004_remove_staffer_birthday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffer',
            options={},
        ),
        migrations.AddField(
            model_name='staffer',
            name='img',
            field=models.ImageField(default=1, upload_to='static/bootstrap/img/'),
            preserve_default=False,
        ),
    ]
