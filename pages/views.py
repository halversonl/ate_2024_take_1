from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1>i hate programming so god damn much</h1>")
    return render(request, "homepage.html")

def about_view(*args, **kwargs):
    return HttpResponse("<h1>this project is about making me as miserable as humanly fucking possible</h1>")
