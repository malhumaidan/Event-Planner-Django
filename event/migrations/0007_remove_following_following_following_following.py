# Generated by Django 4.1.2 on 2022-11-17 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("event", "0006_remove_following_followers_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="following",
            name="following",
        ),
        migrations.AddField(
            model_name="following",
            name="following",
            field=models.ManyToManyField(
                related_name="following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
