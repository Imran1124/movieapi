from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class MovieViews(viewsets.ModelViewSet):
    filter_backends=(DjangoFilterBackend,filters.SearchFilter,)
    filter_fields=('id','title',)
    search_fields=['title']
    queryset=MovieModel.objects.all()
    serializer_class=MovieSerializer

class CountryViews(viewsets.ModelViewSet):
    filter_backends=(DjangoFilterBackend,filters.SearchFilter,)
    filter_fields=('id','country_name',)
    search_fields=['country_name']
    queryset=CountryModel.objects.all()
    serializer_class=CountrySerializer

class StateViews(viewsets.ModelViewSet):
    filter_backends=(DjangoFilterBackend,filters.SearchFilter,)
    filter_fields=('id','state_name','country_id')
    search_fields=['state_name']
    queryset=StateModel.objects.all()
    serializer_class=StateSerializer

class CityViews(viewsets.ModelViewSet):
    filter_backends=(DjangoFilterBackend,filters.SearchFilter,)
    filter_fields=('id','city_name','state_id')
    search_fields=['country_name']
    queryset=CityModel.objects.all()
    serializer_class=CitySerializer


class SingupViews(viewsets.ModelViewSet):
    filter_backends=(DjangoFilterBackend,filters.SearchFilter,)
    filter_fields=('id','name')
    search_fields=['name','email','mobile']
    queryset=SingupModel.objects.all()
    serializer_class=SingupSerializer
