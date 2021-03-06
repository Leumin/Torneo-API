from django.db import transaction
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


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'fecha_fundacion', 'esquema_habitual', 'logo_equipo', 'estadio', 'jugadores')


class EquipoJugadorSerializer(serializers.ModelSerializer):
    equipo_id = serializers.IntegerField()

    class Meta:
        model = EquipoJugador
        fields = ('id', 'jugador', 'estado', 'dorsal', 'equipo_id')
        read_only_fields = ('jugador',)


class JugadorListarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jugador
        fields = (
            'id', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen',
            'posicion')


class JugadorSerializer(serializers.ModelSerializer):
    equipo_jugador = EquipoJugadorSerializer()

    class Meta:
        model = Jugador
        fields = (
            'id', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'lugar_nacimiento', 'peso', 'estatura', 'imagen',
            'posicion', 'equipo_jugador')

    def create(self, validated_data):
        equipo_jugador = validated_data.pop('equipo_jugador')
        with transaction.atomic():
            jugador = Jugador.objects.create(**validated_data)
            EquipoJugador.objects.create(jugador=jugador, **equipo_jugador)
        return jugador

    def update(self, instance, validated_data):
        equipo_jugador = validated_data.pop('equipo_jugador')
        with transaction.atomic():
            Jugador.objects.update(**validated_data)
            e_j = instance.equipo_jugador
            e_j.equipo = equipo_jugador.get('equipo', e_j.equipo)
            e_j.jugador = equipo_jugador.get('jugador', e_j.jugador)
            e_j.estado = equipo_jugador.get('estado', e_j.estado)
            e_j.dorsal = equipo_jugador.get('dorsal', e_j.dorsal)
            e_j.save()

            return instance


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre')


class EstadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadio
        fields = ('id', 'nombre', 'capacidad', 'ciudad')


class EstadioListarSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(read_only=True)

    class Meta:
        model = Estadio
        fields = ('id', 'nombre', 'capacidad', 'ciudad')


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'fecha_fundacion', 'esquema_habitual', 'logo_equipo', 'estadio')


class EquipoListarSerializer(serializers.ModelSerializer):
    estadio = EstadioListarSerializer(read_only=True)
    jugadores = JugadorSerializer(read_only=True, many=True)

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


class EncuentroDetalleSerializaer(serializers.ModelSerializer):
    equipo_local = EquipoListarSerializer(read_only=True)
    equipo_visitante = EquipoListarSerializer(read_only=True)

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
        fields = ('id', 'partido_jugado', 'jugador', 'equipo')


class JugarPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuentro
        fields = (
            'id', 'temporada', 'estadio', 'fecha_partido_jugado', 'arbitros')


class GoleadoresVerSerializer(serializers.Serializer):
    goles = serializers.IntegerField()
    jugador = serializers.CharField()
    equipo = serializers.CharField()


class AmarillaSerializer(serializers.Serializer):
    jugador = serializers.CharField()
    equipo = serializers.CharField()
    amarillas = serializers.IntegerField()


class RojaSerializer(serializers.Serializer):
    jugador = serializers.CharField()
    equipo = serializers.CharField()
    rojas = serializers.IntegerField()
