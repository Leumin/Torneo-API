from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from rest_framework.exceptions import ValidationError
from rest_framework import serializers


class ModeloBase(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, correo, identidad, primer_nombre, primer_apellido,
                    password=None):
        if not identidad or not primer_nombre or not primer_apellido or not correo:
            raise ValueError('Debe de llenar todos los campos obligatorios')

        user = self.model(
            password=password,
            correo=correo,
            identidad=identidad,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, identidad, primer_nombre, primer_apellido,
                         password):
        usuario = self.create_user(
            password=password,
            correo=correo,
            identidad=identidad,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    identidad = models.CharField(max_length=13, unique=True)
    primer_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    correo = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['identidad', 'primer_nombre', 'primer_apellido']

    def clean(self):
        if len(self.identidad) != 13:
            raise ValidationError('El número de identidad debe ser de 13 digitos')
        if not self.identidad.isdigit():
            raise ValidationError("El número de identidad debe contener únicamente dígitos")

    def __str__(self):
        return self.primer_nombre + " " + self.primer_apellido

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Temporada(ModeloBase):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()


class PosicionJugador(ModeloBase):
    descripcion = models.CharField(max_length=50)


class Jugador(ModeloBase):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=50, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    estatura = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to="Jugadores", blank=True)
    posicion = models.ForeignKey(PosicionJugador, on_delete=models.PROTECT)


class Ciudad(ModeloBase):
    nombre = models.CharField(max_length=50)


class Estadio(ModeloBase):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)


class Equipo(ModeloBase):
    nombre = models.CharField(max_length=50)
    fecha_fundacion = models.DateField()
    esquema_habitual = models.CharField(max_length=20, blank=True)
    logo_equipo = models.ImageField(upload_to="Logos", blank=True)
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT)
    jugadores = models.ManyToManyField(Jugador, through='EquipoJugador')

    def __str__(self):
        return self.nombre


class EquipoJugador(ModeloBase):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    jugador = models.ForeignKey(Jugador, on_delete=models.PROTECT)
    estado = models.BooleanField()
    dorsal = models.IntegerField()


class Arbitro(ModeloBase):
    ARBITRO_PRINCIPAL = 1
    ARBITRO_ASISTENTE_1 = 2
    ARBITRO_ASISTENTE_2 = 3
    CUARTO_ARBITRO = 4
    QUINTO_ARBITRO = 5
    SEXTO_ARBITRO = 6

    POSICION_ARBITRO = (
        (ARBITRO_PRINCIPAL, 'Arbitro Principal'),
        (ARBITRO_ASISTENTE_1, 'Arbitro Asistente 1'),
        (ARBITRO_ASISTENTE_2, 'Arbitro Asistente 2'),
        (CUARTO_ARBITRO, 'Cuarto Arbitro'),
        (QUINTO_ARBITRO, 'Quinto Arbitro'),
        (SEXTO_ARBITRO, 'Sexto Arbitro'),
    )
    nombre = models.CharField(max_length=50)
    posicion = models.PositiveSmallIntegerField(choices=POSICION_ARBITRO)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(upload_to="Arbitros", blank=True)


class Encuentro(ModeloBase):
    id = models.AutoField(primary_key=True)
    fecha_encuentro = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='equipo_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='equipo_visitante')
    temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT)
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT, null=True)
    fecha_partido_jugado = models.DateTimeField(null=True)
    arbitros = models.ManyToManyField(Arbitro)
    equipo_jugador = models.ManyToManyField(EquipoJugador)


class Amonestaciones(ModeloBase):
    AMARILLA = 1
    ROJA = 2
    TIPOS_AMONESTACIONES = (
        (AMARILLA, 'Amarilla'),
        (ROJA, 'roja'),
    )
    amonestacion = models.PositiveSmallIntegerField(choices=TIPOS_AMONESTACIONES)
    partido_jugado = models.ForeignKey(Encuentro, on_delete=models.PROTECT)
    jugador = models.ForeignKey(EquipoJugador, on_delete=models.PROTECT)


class Goles(ModeloBase):
    partido_jugado = models.ForeignKey(Encuentro, on_delete=models.PROTECT)
    jugador = models.ForeignKey(EquipoJugador, on_delete=models.PROTECT)


class Entrenador(ModeloBase):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField(upload_to="Entrenador", blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

