from django.db import models


class ModeloBase(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Temporada(ModeloBase):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()


class PosicionJugador(ModeloBase):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)


class Jugador(ModeloBase):
    id = models.AutoField(primary_key=True)
    nombre_jugador = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=50, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    estatura = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.URLField(blank=True)
    posicion = models.ForeignKey(PosicionJugador, on_delete=models.PROTECT)


class Ciudad(ModeloBase):
    id = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=50)


class Estadio(ModeloBase):
    id = models.AutoField(primary_key=True)
    nombre_estadio = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)


class Equipo(ModeloBase):
    id = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=50)
    fecha_fundacion = models.DateField()
    esquema_habitual = models.CharField(max_length=20, blank=True)
    logo_equipo = models.URLField(blank=True)
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT)
    jugadores = models.ManyToManyField(Jugador, through='EquipoJugador')


class EquipoJugador(ModeloBase):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    jugador = models.ForeignKey(Jugador, on_delete=models.PROTECT)
    estado = models.BooleanField()
    dorsal = models.IntegerField()


class PosicionArbitro(ModeloBase):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)


class Arbitro(ModeloBase):
    id = models.AutoField(primary_key=True)
    nombre_arbitro = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=50, blank=True)
    imagen = models.URLField(blank=True)


class ArregloEncuentro(ModeloBase):
    id = models.AutoField(primary_key=True)
    fecha_encuentro = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='equipo_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='equipo_visitante')
    temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT)


class PartidoJugado(ModeloBase):
    id = models.AutoField(primary_key=True)
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT)
    encuentro = models.ForeignKey(ArregloEncuentro, on_delete=models.PROTECT)
    fecha = models.DateTimeField()
    arbitros = models.ManyToManyField(Arbitro)
    equipo_jugador = models.ManyToManyField(EquipoJugador)


class TipoAmonestaciones(ModeloBase):
    id = models.AutoField(primary_key=True)
    descripcion_amonestacion = models.CharField(max_length=50)


class Amonestaciones(ModeloBase):
    amonestacion = models.ForeignKey(TipoAmonestaciones, on_delete=models.PROTECT)
    partido_jugado = models.ForeignKey(PartidoJugado, on_delete=models.PROTECT)
    jugador = models.ForeignKey(EquipoJugador, on_delete=models.PROTECT)


class Goles(ModeloBase):
    partido_jugado = models.ForeignKey(PartidoJugado, on_delete=models.PROTECT)
    jugador = models.ForeignKey(EquipoJugador, on_delete=models.PROTECT)