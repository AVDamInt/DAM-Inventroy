# Generated by Django 4.2 on 2023-04-03 10:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="device",
            name="test_id",
        ),
    ]
