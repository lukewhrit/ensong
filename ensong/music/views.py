import musicbrainzngs
from dateutil.parser import parse
from django.views.generic import ListView

from .models import Album, Artist, Review


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
        mbid = self.kwargs.get("pk")

        musicbrainzngs.set_useragent("ensong", "v0.1.0a", "lukewhrit@proton.me")

        result = musicbrainzngs.get_release_group_by_id(id=mbid, includes=["artists", "tags"])

        context["album"] = Album.objects.get_or_create(
            mbid=mbid,
            defaults={
                "mbid": result["release-group"]["id"],
                "name": result["release-group"]["title"],
                "release_date": parse(result["release-group"]["first-release-date"]),
                "artist": Artist.objects.get_or_create(
                    mbid=result["release-group"]["artist-credit"][0]["artist"]["id"],
                    defaults={
                        "mbid": result["release-group"]["artist-credit"][0]["artist"]["id"],
                        "name": result["release-group"]["artist-credit"][0]["artist"]["name"],
                    },
                )[0],
            },
        )[0]

        return context

    def get_queryset(self):
        return Review.objects.filter(album=self.kwargs.get("pk"))
