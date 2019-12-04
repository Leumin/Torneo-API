import datetime
import pprint

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from API_torneo.models import Equipo, Temporada
from API_torneo.serializers import EquipoSerializer


class ViewCrearEncuentros(APIView):

    def get(self, request, id_temporada, format=None):
        temporada_id = 1
        query_equipo = Equipo.objects.all()
        equipo = []
        for e in query_equipo:
            equipo.append(e.nombre)
        print(equipo)
        temporada = Temporada.objects.get(id=temporada_id).fecha_inicio
        partidos = []
        resultados = {}
        num_semanas = len(equipo) - 1
        mitad_equipos = int((len(equipo)-1)/2)
        dias = 0
        contador = 1
        for x in range(num_semanas*2):
            if x < num_semanas:
                for i in range(mitad_equipos):
                    equipo_local = equipo[mitad_equipos - i]
                    equipo_visita = equipo[mitad_equipos + i + 1]
                    resultados[str(equipo_local)] = {str(x): equipo_local}
                    resultados[str(equipo_visita)] = {str(x): equipo_visita}

                    if i < int(mitad_equipos/2):
                        dias += 1
                        nueva_fecha = temporada + datetime.timedelta(days=dias)
                        dias = 0
                    else:
                        nueva_fecha = temporada + datetime.timedelta(days=dias)

            dias += 5

            if contador == 1:
                equipo.pop(0)
                contador = 0

            temporal = equipo.pop(0)
            equipo.append(temporal)
            # temporal = equipo[1]
            # for j in range(len(equipo) - 1):
            #     equipo[j] = equipo[j+1]
            # equipo[len(equipo)-1] = temporal
            print(equipo)

        return Response(status=status.HTTP_204_NO_CONTENT)