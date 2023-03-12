from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse("home page")


def About(request):
    return HttpResponse("about us")


def contact(request):
    return HttpResponse("contact us ")


def link(request):
    return HttpResponse("link test")
