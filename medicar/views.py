from django.shortcuts import render
from rest_framework.views import APIView
from medicar.models import Agenda, Consulta, Horario
from rest_framework.response import Response
from medicar.serializer import AgendaSerializer, ConsultaSerializer
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view


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
        dados_agenda = Agenda.objects.get(pk=req['agenda_id'])
        nova_consulta =  Consulta.objects.create(dia=dados_agenda.dia, horario=dados_horario.horario, agenda=dados_agenda)
        nova_consulta.save()
        dados_horario.agendado = True
        dados_horario.save()
        serializer = ConsultaSerializer(nova_consulta)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        print(request.GET.get('id'))
        try:
            consulta = self.get_queryset().get()
        except:
            raise APIException("Consulta não localizada")
        consulta.delete()
        dados_horario = Horario.objects.get(horario = consulta.horario)
        dados_horario.agendado = False
        dados_horario.save()
        return Response()

class AgendaView(APIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return Agenda.objects.all()
    
    def get(self, request, *args, **kwargs):

        agendas = self.get_queryset()

        if request.GET.get('medico'):
            agendas = agendas.filter(medico__id=request.GET.get('medico'))

        serializer = AgendaSerializer(agendas, many=True)
        return Response(serializer.data)