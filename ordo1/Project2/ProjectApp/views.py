from django.shortcuts import render
from django.http import HttpResponse


def Gia(request):
    return HttpResponse


def Gone_Girl(request):
    return HttpResponse


def dynamic_world(request, fuck):
    return HttpResponse(fuck)
