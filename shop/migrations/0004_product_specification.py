# Generated by Django 4.1.7 on 2023-04-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_product_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="specification",
            field=models.TextField(blank=True, null=True),
        ),
    ]
