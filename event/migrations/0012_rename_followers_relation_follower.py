# Generated by Django 4.1.2 on 2022-11-23 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0011_rename_followers_relation_followers_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="relation",
            old_name="followers",
            new_name="follower",
        ),
    ]
