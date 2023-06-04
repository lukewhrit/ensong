from django.contrib import admin
from ensong.music.models import User, Artist, Genre, Album

# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(User)
