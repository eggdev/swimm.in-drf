# Generated by Django 3.2.5 on 2021-07-24 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_trainingsession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainingsession',
            old_name='sets',
            new_name='workout_sets',
        ),
    ]
