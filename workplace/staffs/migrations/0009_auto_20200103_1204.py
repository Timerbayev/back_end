# Generated by Django 2.0.5 on 2020-01-03 06:04

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0008_auto_20200102_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(default='', max_length=100)),
                ('data', models.DateField()),
                ('place', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterModelManagers(
            name='staffer',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='staffer',
            old_name='specialization',
            new_name='occupation',
        ),
        migrations.AddField(
            model_name='staffer',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='staffer',
            name='scientific_degree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='staffer',
            name='education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffs.Education'),
        ),
    ]