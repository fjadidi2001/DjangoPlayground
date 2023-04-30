from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return HttpResponse("Home Page")


def About(request):
    return HttpResponse("about us")


def contact(request):
    return HttpResponse("contact us ")


def link(request):
    return HttpResponse("link test")
