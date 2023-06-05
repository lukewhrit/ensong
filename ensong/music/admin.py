from django.contrib import admin
from ensong.music.models import Review, Artist, Genre, Album

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fields = ["name", "image", "mbid"]
    search_fields = ["name"]
    list_display = ["name", "mbid"]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ["artist", "name", "mbid", "release_date", "genre"]
    search_fields = ["name", "artist", "release_date", "genre"]
    list_display = ["name", "artist"]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ["name"]
    search_fields = ["name"]
    list_display = ["name"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = ["author", "stars", "album", "pub_date", "content"]
    search_fields = ["content", "author", "album", "content"]
    list_display = ["author", "album"]
