# Generated by Django 4.1 on 2022-08-05 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exercise", old_name="coach_id", new_name="coach",
        ),
    ]
