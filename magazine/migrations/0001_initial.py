# Generated by Django 4.2.6 on 2023-10-17 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Marka",
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
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Autocar",
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
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="img/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(blank=True, null=True, verbose_name="Цена"),
                ),
                (
                    "data_created",
                    models.DateTimeField(verbose_name="Дата последнего изменения"),
                ),
                (
                    "marka",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="magazine.marka",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Автомобиль",
                "verbose_name_plural": "Автомобили",
            },
        ),
    ]