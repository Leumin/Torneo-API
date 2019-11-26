from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *


class ViewCrearUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializer


class ViewJugador(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) #verifica que los usuarios esten authenticados para hacer uso de la view
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


class ViewTemporada(viewsets.ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer


class ViewPosicionJugador(viewsets.ModelViewSet):
    queryset = PosicionJugador.objects.all()
    serializer_class = PosicionJugadorSerializer
