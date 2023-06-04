from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {
        "home_page": "link-secondary",
    })

def members(request):
    return render(request, "pages/members.html", {
        "members_page": "link-secondary",
    })
