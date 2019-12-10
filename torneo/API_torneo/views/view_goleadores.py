from API_torneo.models import *
from API_torneo.serializers import *
from rest_framework.views import APIView
from django.db.models import Count
from django.http import JsonResponse


class ViewGoleadores(APIView):

    def get(self, request):
        data = []
        goles = Goles.objects.values('jugador__jugador__nombre', 'jugador__equipo__nombre').annotate(
            goles=Count('jugador'))
        serializers__class = GoleadoresSerializer
        for x, contenido in enumerate(goles):
            data.append({'jugador': contenido['jugador__jugador__nombre'],
                         'equipo': contenido['jugador__equipo__nombre'],
                         'goles': contenido['goles']})
        # print(data)
        serializers = GoleadoresSerializer(data=data, many=True)
        if serializers.is_valid():
            return JsonResponse(serializers.data, safe=False)
