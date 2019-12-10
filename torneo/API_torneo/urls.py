from django.urls import path, include

from API_torneo.views.crear_encuentros import ViewCrearEncuentros, ViewListarEncuentros
from API_torneo.views.views_generales import ViewCrearUsuario
from API_torneo.views import views_generales
from rest_framework import routers
from API_torneo.views.crear_amonestaciones import ViewCrearAmonestacion
from API_torneo.views import crear_amonestaciones
from API_torneo.views.crear_gol import ViewCrearGol
from API_torneo.views.view_goleadores import ViewGoleadores
from API_torneo.views.view_amonestaciones import ViewAmonestacionesAmarillas, ViewAmonestacionesRojas

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
    path('api/', include(router.urls)),
    path('api/usuarios/', ViewCrearUsuario.as_view(), name='crear_usuario'),
    path('api/encuentros/generar/<int:id_temporada>', ViewCrearEncuentros.as_view(), name='crear_encuentros'),
    path('api/encuentros/listar/<int:id_temporada>', ViewListarEncuentros.as_view(), name='listar_encuentros'),
    path('api/amonestaciones/crear/', ViewCrearAmonestacion.as_view(), name='crear_amonestaciones'),
    path('api/goles/crear/', ViewCrearGol.as_view(), name='crear_gol'),
    path('api/goles/ver/', ViewGoleadores.as_view(), name='ver_goleadores'),
    path('api/amonestaciones/amarillas/', ViewAmonestacionesAmarillas.as_view(), name='ver_amonestaciones_amarillas'),
    path('api/amonestaciones/rojas/', ViewAmonestacionesRojas.as_view(), name='ver_amonestaciones_rojas')
]
