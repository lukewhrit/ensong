from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {
        "home_page": "link-secondary",
    })

def tos(request):
    return render(request, "pages/tos.html")

def privacy(request):
    return render(request, "pages/privacy.html")

def faqs(request):
    return render(request, "pages/faqs.html")


def members(request):
    return render(request, "pages/members.html", {
        "members_page": "link-secondary",
    })
