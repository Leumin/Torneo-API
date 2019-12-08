from rest_framework import generics
from API_torneo.serializers import AmonestacionesCrearSerializer


class ViewCrearAmonestacion(generics.CreateAPIView):
    serializer_class = AmonestacionesCrearSerializer
