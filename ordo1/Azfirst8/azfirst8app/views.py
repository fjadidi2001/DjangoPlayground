from django.shortcuts import render
from django.http import HttpResponse


def saturday(request):
    return HttpResponse('this is saturday')


def sunday(request):
    return HttpResponse('this is sunday')


def monday(request):
    return HttpResponse('this is monday')


