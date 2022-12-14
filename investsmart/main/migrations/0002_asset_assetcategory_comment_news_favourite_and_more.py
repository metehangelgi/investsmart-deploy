# Generated by Django 4.1.2 on 2022-11-13 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Asset",
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
                ("asset_name", models.CharField(max_length=200)),
                ("asset_ticker", models.CharField(max_length=20)),
                ("view_count", models.IntegerField(default=0)),
                ("photo_link", models.URLField(default=None)),
                ("market_size", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Assets",
            },
        ),
        migrations.CreateModel(
            name="AssetCategory",
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
                ("category_name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("comment_text", models.TextField()),
                (
                    "date_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date published"
                    ),
                ),
                ("like_count", models.IntegerField(default=0)),
                ("imported_from", models.CharField(max_length=200)),
                (
                    "asset",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.asset",
                        verbose_name="Asset",
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.comment"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=200)),
                ("link", models.URLField(default=None)),
                (
                    "date_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date published"
                    ),
                ),
                ("source", models.CharField(max_length=200)),
                (
                    "asset",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="main.asset",
                        verbose_name="Asset",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Newss",
            },
        ),
        migrations.CreateModel(
            name="favourite",
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
                (
                    "favourite_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date published"
                    ),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.asset",
                        verbose_name="Asset",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Favourites",
            },
        ),
        migrations.CreateModel(
            name="CommentLike",
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
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.comment"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Favourites",
            },
        ),
        migrations.AddField(
            model_name="asset",
            name="asset_category",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="main.assetcategory",
                verbose_name="Category",
            ),
        ),
    ]
