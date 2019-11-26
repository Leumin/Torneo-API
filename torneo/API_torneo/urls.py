from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jugadores', views.ViewJugador)
router.register('temporadas', views.ViewTemporada)
router.register('posiciones-jugador', views.ViewPosicionJugador)
router.register('ciudad',views.ViewCiudad)
router.register('estadio',views.ViewEstadio)
router.register('equipo',views.ViewEquipo)
router.register('arbitro',views.ViewArbitro)
urlpatterns = [
    path('', include(router.urls))
]