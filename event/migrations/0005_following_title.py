# Generated by Django 4.1.2 on 2022-11-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0004_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="following",
            name="title",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
