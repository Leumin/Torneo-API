from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class ViewJugador(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


class ViewTemporada(viewsets.ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer


class ViewPosicionJugador(viewsets.ModelViewSet):
    queryset = PosicionJugador.objects.all()
    serializer_class = PosicionJugadorSerializer


class ViewCiudad(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class ViewEstadio(viewsets.ModelViewSet):
    queryset = Estadio.objects.all()
    serializer_class = EstadioSerializer


class ViewEquipo(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class ViewArbitro(viewsets.ModelViewSet):
    queryset = Arbitro.objects.all()
    serializer_class = ArbitroSerializer
