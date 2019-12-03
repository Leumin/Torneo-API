from django.urls import path, include

from API_torneo.views.views_generales import ViewCrearUsuario
from API_torneo.views import views_generales
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jugadores', views_generales.ViewJugador)
router.register('temporadas', views_generales.ViewTemporada)
router.register('posiciones-jugador', views_generales.ViewPosicionJugador)
router.register('ciudad', views_generales.ViewCiudad)
router.register('estadio', views_generales.ViewEstadio)
router.register('equipo', views_generales.ViewEquipo)
router.register('arbitro', views_generales.ViewArbitro)
router.register('entrenador', views_generales.ViewEntrenador)

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/', ViewCrearUsuario.as_view(), name='crear_usuario')
]