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


class TemporadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'url','fecha_inicio', 'fecha_final')


class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugador
        fields = (
            'id', 'url','nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen',
            'posicion')


class PosicionJugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PosicionJugador
        fields = ('id', 'url', 'descripcion')


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id','url', 'nombre')


class EstadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estadio
        fields = ('id','url', 'nombre', 'capacidad', 'ciudad')


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id','url' ,'nombre', 'fecha_fundacion', 'esquema_habitual', 'logo_equipo', 'estadio', 'jugadores')


class ArbitroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arbitro
        fields = ('id','url', 'nombre', 'posicion', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'imagen')
