# Generated by Django 4.1.3 on 2022-12-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_app', '0002_remove_device_name_device_archiviazione_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='Archiviazione',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Memoria',
        ),
        migrations.AddField(
            model_name='device',
            name='hard_disk',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='memory',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='user_history',
            field=models.ManyToManyField(to='warehouse_app.deviceuser'),
        ),
    ]