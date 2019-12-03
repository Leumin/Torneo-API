from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from API_torneo.serializers import *
from API_torneo.models import *


class ViewVerTablaPosicion(APIView):


    def get(self, request, format=None):
        pass
