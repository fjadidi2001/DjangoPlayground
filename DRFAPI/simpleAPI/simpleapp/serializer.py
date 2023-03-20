from rest_framework import serializers
from .models import Apis


class ApisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apis
        fields = ('name', 'description')
