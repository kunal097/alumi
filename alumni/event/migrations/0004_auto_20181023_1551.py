# Generated by Django 2.1.2 on 2018-10-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='schedule',
            field=models.DateField(),
        ),
    ]