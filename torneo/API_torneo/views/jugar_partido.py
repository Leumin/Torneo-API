from django.db.models import QuerySet
from rest_framework import generics, status
from rest_framework.generics import UpdateAPIView, get_object_or_404

from API_torneo.serializers import JugarPartidoSerializer
from API_torneo.models import Encuentro
from rest_framework.response import Response
from rest_framework.views import APIView


class ViewJugarPartido(generics.UpdateAPIView):
    serializer_class = JugarPartidoSerializer
    queryset = None

    def put(self, request, id_encuentro, *args, **kwargs):
        encuentro = Encuentro.objects.get(id=id_encuentro)
        temporada = request.data['temporada']
        estadio = request.data['estadio']
        fecha_partido_jugado = request.data['fecha_partido_jugado']
        arbitros = request.data['arbitros']

        data = {'temporada': temporada, 'estadio': estadio, 'fecha_partido_jugado': fecha_partido_jugado, 'arbitros': [arbitros],
                'encuentro': id_encuentro}
        serializer = JugarPartidoSerializer(instance=encuentro, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            encuentro = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


