# Generated by Django 4.1.3 on 2022-12-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_app', '0003_remove_device_archiviazione_remove_device_memoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(blank=True, choices=[('Attivo', 'Attivo'), ('Storico', 'Storico')], default='Attivo', max_length=20, null=True),
        ),
    ]
