# Generated by Django 4.1.3 on 2022-12-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_app', '0008_device_status_bol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='status_bol',
            field=models.BooleanField(default=True),
        ),
    ]
