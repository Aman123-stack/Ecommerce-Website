# Generated by Django 4.1.5 on 2023-01-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_rename_color_name_sizevariant_size_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color_variant",
            field=models.ManyToManyField(blank=True, to="products.colorvariant"),
        ),
        migrations.AlterField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(blank=True, to="products.sizevariant"),
        ),
    ]
