# Generated by Django 4.1.2 on 2022-11-30 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_comment_imported_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='favourite_count',
        ),
        migrations.RemoveField(
            model_name='assetcategory',
            name='favourite_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like_count',
        ),
    ]