# Generated by Django 4.1.2 on 2022-11-17 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0008_following_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="following",
            old_name="following",
            new_name="users",
        ),
    ]
