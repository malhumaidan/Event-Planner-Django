# Generated by Django 4.1.2 on 2022-10-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_alter_event_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(blank=True, upload_to="media"),
        ),
    ]
