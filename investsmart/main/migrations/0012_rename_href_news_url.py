# Generated by Django 4.1.2 on 2022-11-14 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_rename_date_time_news_published_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="href",
            new_name="url",
        ),
    ]
