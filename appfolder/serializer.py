from rest_framework import serializers
from .models import *
from rest_framework import exceptions


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=MovieModel
        fields="__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=CountryModel
        fields="__all__"

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StateModel
        fields="__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=CityModel
        fields="__all__"

class SingupSerializer(serializers.ModelSerializer):
    # country = CountrySerializer( read_only=True)
    # state = StateSerializer(read_only=True)
    # city = CitySerializer( read_only=True)
    class Meta:
        model=SingupModel
        fields="__all__"
