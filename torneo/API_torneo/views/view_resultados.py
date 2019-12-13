from rest_framework import status
from API_torneo.models import *
from API_torneo.serializers import *
from rest_framework.views import APIView
from django.db.models import Count, Subquery, Q
from django.db import connection
from rest_framework.response import Response


class ViewResultado(APIView):

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT "
                           "`API_torneo_encuentro`.`id` AS `id_partido_jugado`,"
                           "`API_torneo_encuentro`.`equipo_local_id` AS `equipo_local`,"
                           "`equipo_local`.`nombre` AS Nombre_Local,"
                           "(SELECT COUNT(0) FROM `torneo`.`API_torneo_goles`"
                           "WHERE `torneo`.`API_torneo_goles`.`partido_jugado_id` = `API_torneo_encuentro`.`id`"
                           "AND `torneo`.`API_torneo_goles`.`equipo_id` = `API_torneo_encuentro`.`equipo_local_id`) "
                           "AS `resultado_local`, `API_torneo_encuentro`.`equipo_visitante_id`"
                           "AS `equipo_visita`,"
                           "`equipo_visitante`.`nombre` AS Nombre_Visitante,"
                           "(SELECT COUNT(0) FROM `torneo`.`API_torneo_goles`"
                           "WHERE `torneo`.`API_torneo_goles`.`partido_jugado_id` = `API_torneo_encuentro`.`id`"
                           "AND `torneo`.`API_torneo_goles`.`equipo_id` = `API_torneo_encuentro`.`equipo_visitante_id`)"
                           "AS `resultado_visita`"
                           "FROM"
                           "((`torneo`.`API_torneo_encuentro`"
                           "JOIN `torneo`.`API_torneo_equipo` `equipo_local` "
                           "ON (`torneo`.`API_torneo_encuentro`.`equipo_local_id` = `equipo_local`.`id`))"
                           "JOIN `torneo`.`API_torneo_equipo` `equipo_visitante`"
                           "ON(`torneo`.`API_torneo_encuentro`.`equipo_visitante_id` = `equipo_visitante`.`id`))"
                           "WHERE `torneo`.`API_torneo_encuentro`.`fecha_partido_jugado` IS NOT NULL "
                           "ORDER BY `torneo`.`API_torneo_encuentro`.`fecha_encuentro`")

            columns = [col[0] for col in cursor.description]
            return Response([
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ])
