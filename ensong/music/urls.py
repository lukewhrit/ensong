from django.urls import path
from ensong.music.views import index

app_name = "music"
urlpatterns = [
    path("", view=index, name="index"),
]
