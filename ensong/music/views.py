from typing import Any, Dict
from django.views.generic import DetailView, TemplateView
from .models import Album

# Create your views here.
class IndexView(TemplateView):
    template_name = "music/home.html"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album.html"
