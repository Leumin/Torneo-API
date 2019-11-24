from rest_framework import serializers
from .models import *


class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'fecha_inicio', 'fecha_final')


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = (
            'id', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen', 'posicion')


class PosicionJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosicionJugador
        fields = ('id', 'descripcion')

