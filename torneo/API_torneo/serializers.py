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


class PosicionJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosicionJugador
        fields = ('id', 'descripcion')


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = (
            'id', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen',
            'posicion')


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


class EntrenadorSerializer(serializers.ModelSerializer):
    equipo = EquipoSerializer()

    class Meta:
        model = Entrenador
        fields = ('id', 'nombre', 'nacionalidad', 'lugar_nacimiento', 'fecha_nacimiento', 'imagen', 'equipo')


class CrearEntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = ('id', 'nombre', 'nacionalidad', 'lugar_nacimiento', 'fecha_nacimiento', 'imagen', 'equipo')


class EncuentroGenerarSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Encuentro
        fields = ('fecha_encuentro', 'equipo_local', 'equipo_visitante', 'temporada')


class EncuentroListarSerializaer(serializers.ModelSerializer):
    equipo_local = EquipoSerializer(read_only=True)
    equipo_visitante = EquipoSerializer(read_only=True)

    class Meta:
        model = Encuentro
        fields = ('id', 'fecha_encuentro', 'equipo_local', 'equipo_visitante', 'temporada')


class AmonestacionesCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amonestaciones
        fields = ('id', 'amonestacion', 'partido_jugado', 'jugador')


class CrearGolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goles
        fields = ('id','partido_jugado','jugador')


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
