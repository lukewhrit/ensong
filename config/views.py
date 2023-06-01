from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {
        "home_page": "link-secondary",
        "music_page": " link-body-emphasis",
        "members_page": "link-body-emphasis",
        "charts_page": " link-body-emphasis"
    })

def music(request):
    return render(request, "pages/music.html", {
        "home_page": "link-body-emphasis",
        "music_page": " link-secondary",
        "members_page": "link-body-emphasis",
        "charts_page": " link-body-emphasis"
    })

def members(request):
    return render(request, "pages/members.html", {
        "home_page": "link-body-emphasis",
        "music_page": " link-body-emphasis",
        "members_page": "link-secondary",
        "charts_page": " link-body-emphasis"
    })

def charts(request):
    return render(request, "pages/charts.html", {
        "home_page": "link-body-emphasis",
        "music_page": " link-body-emphasis",
        "members_page": "link-body-emphasis",
        "charts_page": " link-secondary"
    })
