# Generated by Django 3.2.5 on 2021-07-20 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='compelete',
            new_name='complete',
        ),
    ]
