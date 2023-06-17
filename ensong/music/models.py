from django.db import models
from django.utils import timezone
from ensong.users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
    mbid = models.UUIDField(_("MusicBrainz ID"), primary_key=True, blank=False, max_length=36)

    name = models.CharField(_("artist name"), max_length=255)
    image = models.ImageField(_("image of artist"), blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(_("genre name"), max_length=255)

    def __str__(self):
        return self.name

class Album(models.Model):
    mbid = models.UUIDField(_("MusicBrainz ID"), primary_key=True, blank=False, max_length=36)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(_("Album name"), max_length=255)
    release_date = models.DateField(_("album release date"))
    genre = models.ManyToManyField(Genre)

    def genres(self):
        return [genre.name for genre in self.genre.all()]

    def average_rating(self):
        return 3

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(_("star rating"), validators=[MaxValueValidator(5), MinValueValidator(1)])
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(_("publish date"), default=timezone.now)
    content = models.CharField(_("review"), max_length=10_000)

    def __str__(self):
        return self.content
