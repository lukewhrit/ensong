from django.urls import path

from . import views

app_name = "music"
urlpatterns = [
    path("", view=views.MusicIndexView.as_view(), name="index"),
    path("<uuid:pk>/", view=views.MusicReviewListView.as_view(), name="album"),
    path("review/", view=views.MusicReviewCreateView.as_view(), name="review"),
    path("<uuid:pk>/delete", view=views.MusicReviewDeleteView, name="review-delete"),
]
