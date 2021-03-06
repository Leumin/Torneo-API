from django.urls import path, include

from API_torneo.views.crear_encuentros import ViewCrearEncuentros, ViewListarEncuentros, ViewDetalleEncuentros
from API_torneo.views.views_generales import ViewCrearUsuario
from API_torneo.views import views_generales
from rest_framework import routers
from API_torneo.views.crear_amonestaciones import ViewCrearAmonestacion
from API_torneo.views import crear_amonestaciones
from API_torneo.views.crear_gol import ViewCrearGol
from API_torneo.views.jugar_partido import ViewJugarPartido
from API_torneo.views.view_goleadores import ViewGoleadores, ViewGoleador
from API_torneo.views.view_amonestaciones import ViewAmonestacionesAmarillas, ViewAmonestacionesRojas
from API_torneo.views.view_resultados import ViewResultado
from API_torneo.views.view_resultado_encuentro import ViewResultadoEncuentro

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
    path('api/encuentros/detalle/<int:id_encuentro>', ViewDetalleEncuentros.as_view(), name='detalle_encuentros'),
    path('api/amonestaciones/crear/', ViewCrearAmonestacion.as_view(), name='crear_amonestaciones'),
    path('api/goles/crear/', ViewCrearGol.as_view(), name='crear_gol'),
    path('api/goles/ver/', ViewGoleadores.as_view(), name='ver_goleadores'),
    path('api/goles/goleador/<int:id_goleador>', ViewGoleador.as_view(), name='ver_goleador'),
    path('api/amonestaciones/amarillas/', ViewAmonestacionesAmarillas.as_view(), name='ver_amonestaciones_amarillas'),
    path('api/encuentro/jugar/<int:id_encuentro>', ViewJugarPartido.as_view(), name='jugar_partido'),
    path('api/amonestaciones/rojas/', ViewAmonestacionesRojas.as_view(), name='ver_amonestaciones_rojas'),
    path('api/resultados/', ViewResultado.as_view()),
    path('api/resultado/<int:id_resultado>', ViewResultadoEncuentro.as_view())

]
