from django.shortcuts import render
from rest_framework.views import APIView
from medicar.models import Consulta, Horario
from rest_framework.response import Response
from medicar.serializer import ConsultaSerializer
from rest_framework.exceptions import APIException

class ConsultasView(APIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return Consulta.objects.all()
    
    def get(self, request, *args, **kwargs):
        consulta = self.get_queryset().filter()
        serializer = ConsultaSerializer(consulta, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        req = request.data
        dados_horario = Horario.objects.get(horario = req['horario'])
        if dados_horario.agendado:
            raise APIException('Horário não disponível, tente outro horário.')
        
