from rest_framework import generics
from API_torneo.serializers import CrearGolSerializer


class ViewCrearGol(generics.CreateAPIView):
    serializer_class = CrearGolSerializer