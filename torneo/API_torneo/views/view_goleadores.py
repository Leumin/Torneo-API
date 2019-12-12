from rest_framework import status

from API_torneo.models import *
from API_torneo.serializers import *
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response


class ViewGoleadores(APIView):
    serializers__class = GoleadoresVerSerializer

    def get(self, request):
        data = []
        goles = Goles.objects.values('jugador__jugador__nombre', 'jugador__equipo__nombre').annotate(
            goles=Count('jugador'))
        for contenido in goles:
            data.append({'jugador': contenido['jugador__jugador__nombre'],
                         'equipo': contenido['jugador__equipo__nombre'],
                         'goles': contenido['goles']})
        serializers = GoleadoresVerSerializer(data=data, many=True)
        if serializers.is_valid():
            return Response(serializers.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
