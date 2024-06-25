# Generated by Django 4.2.13 on 2024-06-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0002_alter_produto_imagem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banners",
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
                ("imagem", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "link_destino",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                ("ativo", models.BooleanField(default=False)),
            ],
        ),
    ]
