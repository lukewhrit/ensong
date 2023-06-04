from django.db import models
from django.utils import timezone
from ensong.users.models import User
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
    name = models.CharField(_("artist name"))
    image = models.ImageField(_("image of artist"))

class Genre(models.Model):
    name = models.CharField(_("genre name"))

class Album(models.Model):
    artist = models.ForeignKey(Artist)
    mbid = models.CharField(_("MusicBrainz ID"), max_length=36)
    release_date = models.DateField(_("album release date"))
    genre = models.ForeignObject(Genre)

    def average_rating(self):
        return 3

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(_("star rating"), max=5, min=1)
    pub_date = models.DateTimeField(_("release date"), default=timezone.now())
    content = models.CharField(_("review"), max_length=10_000)

    def __str__(self):
        return self.content
