import musicbrainzngs
from dateutil.parser import parse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from ensong.music.models import Album, Artist, Review


# Create your views here.
class MusicIndexView(ListView):
    model = Album
    template_name = "music/home.html"
    context_object_name = "albums"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["music_page"] = "link-secondary"

        return context


class MusicReviewListView(ListView):
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


class MusicReviewCreateView(CreateView):
    model = Review
    template_name = "music/review_create.html"
    fields = ["album", "stars", "content"]
    success_url = "/users/~redirect"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def MusicReviewDeleteView(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        if review.author == request.user:
            review.delete()
            return redirect(reverse_lazy("users:redirect"))

    return redirect(reverse_lazy("/"))
