from django.views.generic import ListView
from .models import Album, Review

# Create your views here.
class IndexView(ListView):
    model = Album
    template_name = "music/home.html"
    context_object_name = "albums"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["music_page"] = "link-secondary"

        return context


class ReviewListView(ListView):
    model = Review
    template_name = "music/album.html"
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.filter(mbid=self.kwargs.get("pk"))[0]

        return context

    def get_queryset(self):
        return Review.objects.filter(album=self.kwargs.get("pk"))
