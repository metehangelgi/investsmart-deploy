# Generated by Django 4.1.2 on 2022-11-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_asset_liked_count_assetcategory_liked_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='mentioned_asset',
            field=models.ManyToManyField(blank=True, to='main.news'),
        ),
    ]
