from dataclasses import fields
from rest_framework import serializers
from medicar.models import Agenda, Consulta, Medico

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        depth = 2

class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.StringRelatedField(many=True)
    class Meta:
        model = Agenda
        fields = '__all__'
        depth = 2

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
        depth = 1