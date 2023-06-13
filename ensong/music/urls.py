from django.urls import path
from . import views

app_name = "music"
urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"),
    path("<uuid:pk>/", view=views.AlbumDetailView.as_view(), name="album")
]
