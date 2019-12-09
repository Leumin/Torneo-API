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
        fields = ('id', 'url', 'fecha_inicio', 'fecha_final')


class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugador
        fields = (
            'id', 'url', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen',
            'posicion')


class PosicionJugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PosicionJugador
        fields = ('id', 'url', 'descripcion')


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'url', 'nombre')


class EstadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estadio
        fields = ('id', 'url', 'nombre', 'capacidad', 'ciudad')


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'url', 'nombre', 'fecha_fundacion', 'esquema_habitual', 'logo_equipo', 'estadio', 'jugadores')


class ArbitroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arbitro
        fields = ('id', 'url', 'nombre', 'posicion', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'imagen')


class EntrenadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrenador
        fields = ('id', 'url', 'nombre', 'nacionalidad', 'lugar_nacimiento', 'fecha_nacimiento', 'imagen', 'equipo')


class EncuentroSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Encuentro
        fields = ('fecha_encuentro', 'equipo_local', 'equipo_visitante', 'temporada')


class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewResultado
        fields = ('id_partidos_jugados', 'equipo_local', 'goles_local', 'puntos_del_local', 'equipo_visita',
                  'goles_visita')


class Resultado1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ViewResultados
        fields = ('id_partido_jugado', 'equipo_local', 'resultado_local', 'equipo_visita', 'resultado_visita')


class TablaPosicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewTablaDePosicion
        fields = ('nombre_equipo', 'PG', 'PE', 'PP', 'PJ', 'GF', 'GC', 'PTS')
