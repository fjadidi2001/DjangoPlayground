from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Apis
from .serializer import ApisSerializer


@api_view(['GET'])
def getApis(request):
    food = Apis.objects.all()
    serializer = ApisSerializer(food, many=True)
    return Response(serializer.data)


def postApis(request):
    serial = ApisSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)
