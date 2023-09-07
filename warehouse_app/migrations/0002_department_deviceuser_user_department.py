# Generated by Django 4.2 on 2023-09-06 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, null=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="deviceuser",
            name="user_department",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="warehouse_app.department",
            ),
        ),
    ]
