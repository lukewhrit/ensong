# Generated by Django 4.1.9 on 2023-06-05 01:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, verbose_name="Album name")),
                ("mbid", models.UUIDField(blank=True, verbose_name="MusicBrainz ID")),
                ("release_date", models.DateField(verbose_name="album release date")),
            ],
        ),
        migrations.CreateModel(
            name="Artist",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, verbose_name="artist name")),
                ("mbid", models.UUIDField(blank=True, verbose_name="MusicBrainz ID")),
                ("image", models.ImageField(upload_to="", verbose_name="image of artist")),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, verbose_name="genre name")),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "stars",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="star rating",
                    ),
                ),
                ("pub_date", models.DateTimeField(default=django.utils.timezone.now, verbose_name="release date")),
                ("content", models.CharField(max_length=10000, verbose_name="review")),
                ("album", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="music.album")),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.AddField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="music.artist"),
        ),
        migrations.AddField(
            model_name="album",
            name="genre",
            field=models.ManyToManyField(to="music.genre"),
        ),
    ]
