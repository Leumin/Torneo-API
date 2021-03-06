import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from API_torneo.models import Equipo, Temporada, Encuentro
from API_torneo.serializers import EncuentroGenerarSerializaer, EncuentroListarSerializaer, \
    EncuentroDetalleSerializaer


class ViewCrearEncuentros(APIView):
    serializer_class = EncuentroGenerarSerializaer

    def get(self, request, id_temporada):
        query_equipo = Equipo.objects.all()
        equipo = []
        for e in query_equipo:
            equipo.append(e.pk)
        temporada = Temporada.objects.get(id=id_temporada).fecha_inicio
        resultados = {}
        num_semanas = len(equipo) - 1
        mitad_equipos = int((len(equipo) - 1) / 2)
        dias = 0
        for x in range(num_semanas * 2):
            for i in range(int(len(equipo)/2)):
                equipo_local = equipo[mitad_equipos - i]
                equipo_visita = equipo[mitad_equipos + i + 1]
                if x < num_semanas:
                    resultados[str(equipo_local)] = {str(x): equipo_visita}
                    resultados[str(equipo_visita)] = {str(x): equipo_local}
                else:
                    resultados[str(equipo_local)] = {str(x): equipo_local}
                    resultados[str(equipo_visita)] = {str(x): equipo_visita}

                if i > int(mitad_equipos / 2):
                    dias += 1
                    nueva_fecha = temporada + datetime.timedelta(days=dias)
                    dias -= 1
                else:
                    nueva_fecha = temporada + datetime.timedelta(days=dias)

                data = {'fecha_encuentro': nueva_fecha, 'equipo_local': resultados[str(equipo_local)][str(x)],
                        'equipo_visitante': resultados[str(equipo_visita)][str(x)], 'temporada': id_temporada}
                serializer = EncuentroGenerarSerializaer(data=data)
                if serializer.is_valid():
                    encuentro = serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            dias += 5
            temporal = equipo[0]
            for j in range(len(equipo) - 1):
                equipo[j] = equipo[j + 1]
            equipo[len(equipo) - 1] = temporal

        return Response(status=status.HTTP_200_OK)


class ViewListarEncuentros(APIView):
    def get(self, request, id_temporada):
        encuentros = Encuentro.objects.filter(temporada=id_temporada)
        data = EncuentroListarSerializaer(encuentros, many=True).data
        return Response(data)


class ViewDetalleEncuentros(APIView):
    def get(self, request, id_encuentro):
        encuentros = Encuentro.objects.get(id=id_encuentro)
        data = EncuentroDetalleSerializaer(encuentros).data
        return Response(data)