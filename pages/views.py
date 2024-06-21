from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm


# Create your views here.
def homepage_view(request, *args, **kwargs):
    # return HttpResponse("<h1>i hate programming so god damn much</h1>")
    return render(request, "homepage.html")


def about_view(request, *args, **kwargs):
    return render(request, "about.html")


def upload_file(request):
    pass
