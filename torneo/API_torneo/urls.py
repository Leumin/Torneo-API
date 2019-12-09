from django.urls import path, include

from API_torneo.views.views_generales import ViewCrearUsuario
from API_torneo.views import views_generales
from rest_framework import routers
from API_torneo.views.crear_amonestaciones import ViewCrearAmonestacion
from API_torneo.views import crear_amonestaciones
from API_torneo.views.crear_gol import ViewCrearGol

router = routers.DefaultRouter()
router.register('jugadores', views_generales.ViewJugador)
router.register('temporadas', views_generales.ViewTemporada)
router.register('posiciones-jugador', views_generales.ViewPosicionJugador)
router.register('ciudades', views_generales.ViewCiudad)
router.register('estadios', views_generales.ViewEstadio)
router.register('equipos', views_generales.ViewEquipo)
router.register('arbitros', views_generales.ViewArbitro)
router.register('entrenadores', views_generales.ViewEntrenador)

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/', ViewCrearUsuario.as_view(), name='crear_usuario'),
    path('encuentros/generar/<int:id_temporada>', ViewCrearEncuentros.as_view(), name='crear_encuentros'),
    path('encuentros/listar/<int:id_temporada>', ViewListarEncuentros.as_view(), name='listar_encuentros'),
    path('amonestaciones/crear/', ViewCrearAmonestacion.as_view(), name='crear_amonestaciones'),
    path('goles/crear/', ViewCrearGol.as_view(), name='crear_gol')
]