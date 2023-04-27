# Generated by Django 4.1.7 on 2023-04-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_order_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_items",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.CharField(max_length=10, null=True),
        ),
    ]