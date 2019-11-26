from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('correo', 'password', 'identidad', 'primer_nombre', 'primer_apellido')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            usuario = Usuario(
                correo=validated_data['correo'],
                identidad=validated_data['identidad'],
                primer_nombre=validated_data['primer_nombre'],
                primer_apellido=validated_data['primer_apellido']
            )
            usuario.set_password(validated_data['password'])
            usuario.save()
            return usuario


class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'fecha_inicio', 'fecha_final')


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = (
            'id', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen',
            'posicion')


class PosicionJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosicionJugador
        fields = ('id', 'descripcion')


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre')


class EstadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadio
        fields = ('id', 'nombre', 'capacidad', 'ciudad')


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'fecha_fundacion', 'esquema_habitual', 'logo_equipo', 'estadio', 'jugadores')


class ArbitroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbitro
        fields = ('id', 'nombre', 'posicion', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'imagen')
