# Generated by Django 2.1.2 on 2018-10-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='paasout_year',
            field=models.DateField(),
        ),
    ]