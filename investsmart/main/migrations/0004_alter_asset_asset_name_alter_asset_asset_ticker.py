# Generated by Django 4.1.2 on 2022-11-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_asset_last_price_alter_asset_asset_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="asset_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="asset",
            name="asset_ticker",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
