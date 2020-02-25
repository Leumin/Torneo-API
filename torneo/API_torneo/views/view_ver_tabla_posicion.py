from operator import itemgetter

from django.db import connection
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from API_torneo.serializers import *
from API_torneo.models import *


class ViewVerTablaPosicion(APIView):

    def get(self, request, format=None):
        data = {}
        count = 0
        with connection.cursor() as cursor:
            resultado = cursor.execute("SELECT "
                                       "`API_torneo_encuentro`.`id` AS `id_partido_jugado`,"
                                       "`API_torneo_encuentro`.`equipo_local_id` AS `equipo_local`,"
                                       "`equipo_local`.`nombre` AS Nombre_Local,"
                                       "(SELECT COUNT(0) FROM `torneo`.`API_torneo_goles`"
                                       "WHERE `torneo`.`API_torneo_goles`.`partido_jugado_id` = "
                                       "`API_torneo_encuentro`.`id`"
                                       "AND `torneo`.`API_torneo_goles`.`equipo_id` = "
                                       "`API_torneo_encuentro`.`equipo_local_id`) "
                                       "AS `resultado_local`, `API_torneo_encuentro`.`equipo_visitante_id`"
                                       "AS `equipo_visita`,"
                                       "`equipo_visitante`.`nombre` AS Nombre_Visitante,"
                                       "(SELECT COUNT(0) FROM `torneo`.`API_torneo_goles`"
                                       "WHERE `torneo`.`API_torneo_goles`.`partido_jugado_id` = "
                                       "`API_torneo_encuentro`.`id`"
                                       "AND `torneo`.`API_torneo_goles`.`equipo_id` = "
                                       "`API_torneo_encuentro`.`equipo_visitante_id`)"
                                       "AS `resultado_visita`"
                                       "FROM"
                                       "((`torneo`.`API_torneo_encuentro`"
                                       "JOIN `torneo`.`API_torneo_equipo` `equipo_local` "
                                       "ON (`torneo`.`API_torneo_encuentro`.`equipo_local_id` = `equipo_local`.`id`))"
                                       "JOIN `torneo`.`API_torneo_equipo` `equipo_visitante`"
                                       "ON(`torneo`.`API_torneo_encuentro`.`equipo_visitante_id` ="
                                       " `equipo_visitante`.`id`))"
                                       "WHERE `torneo`.`API_torneo_encuentro`.`fecha_partido_jugado` IS NOT NULL "
                                       "ORDER BY `torneo`.`API_torneo_encuentro`.`fecha_encuentro`")

            columns = [col[0] for col in cursor.description]
            dt = [dict(zip(columns, row))
                  for row in cursor.fetchall()]
            # print(dt)
        equipos = Equipo.objects.all()
        for equipo in equipos:
            for value in dt:
                if equipo.id == value['equipo_local']:
                    if value['resultado_local'] > value['resultado_visita']:
                        count += 3
                    elif value['resultado_local'] < value['resultado_visita']:
                        count += 0
                    else:
                        count += 1

                if equipo.id == value['equipo_visita']:
                    if value['resultado_visita'] > value['resultado_local']:
                        count += 3
                    elif value['resultado_visita'] < value['resultado_local']:
                        count += 0
                    else:
                        count += 1

            data[str(equipo)] = {'pts': count}
            count = 0
            # print(sorted(data[str(equipo)]['pts'].iteritems(), key=itemgetter(1), reverse=True))
        return Response(data)

