from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from API_torneo.serializers import *
from API_torneo.models import *


class ViewCrearUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializer


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
    serializer_class = EstadioListarSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return EstadioSerializer
        return super().get_serializer_class()


class ViewEquipo(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoListarSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return EquipoSerializer
        return super().get_serializer_class()


class ViewArbitro(viewsets.ModelViewSet):
    queryset = Arbitro.objects.all()
    serializer_class = ArbitroSerializer


class ViewEntrenador(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CrearEntrenadorSerializer
        return super().get_serializer_class()
