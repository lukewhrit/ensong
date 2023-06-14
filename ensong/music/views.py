from django.views.generic import DetailView, ListView
from .models import Album

# Create your views here.
class IndexView(ListView):
    model = Album
    template_name = "music/home.html"
    context_object_name = "albums"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["music_page"] = "link-secondary"

        return context


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album.html"
