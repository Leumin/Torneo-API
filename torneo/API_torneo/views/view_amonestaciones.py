from API_torneo.models import *
from API_torneo.serializers import *
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status


class ViewAmonestacionesAmarillas(APIView):
    serializers__class = AmarillaSerializer

    def get(self, request):
        data = []

        amarillas = Amonestaciones.objects.filter(amonestacion__exact=1). \
            values('jugador__jugador__nombre', 'jugador__equipo__nombre'). \
            annotate(amarillas=Count('jugador'))

        for i in amarillas:
            data.append(
                {'jugador': i['jugador__jugador__nombre'],
                 'equipo': i['jugador__equipo__nombre'],
                 'amarillas': i['amarillas']})
        serializers = AmarillaSerializer(data=data, many=True)
        if serializers.is_valid():
            return Response(serializers.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ViewAmonestacionesRojas(APIView):
    serializers_class = RojaSerializer

    def get(self, request):
        data = []
        rojas = Amonestaciones.objects.filter(amonestacion__exact=2). \
            values('jugador__jugador__nombre', 'jugador__equipo__nombre'). \
            annotate(rojas=Count('jugador'))

        for i in rojas:
            data.append(
                {'jugador': i['jugador__jugador__nombre'],
                 'equipo': i['jugador__equipo__nombre'],
                 'rojas': i['rojas']})
        serializers = RojaSerializer(data=data, many=True)
        if serializers.is_valid():
            return Response(serializers.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
