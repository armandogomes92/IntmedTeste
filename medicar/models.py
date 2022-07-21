import email
from enum import unique
from hashlib import blake2b
from pickle import FALSE
from re import T
from tkinter import CASCADE
from django.db import models
from django.forms import EmailField, IntegerField



class Medico(models.Model):
    nome = models.CharField(max_length=35)
    crm =  models.IntegerField(unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.nome


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, models.CASCADE)
    dia = models.DateField()
    class Meta:
        unique_together = ('medico', 'dia')

    def __str__(self) -> str:
        return str(self.dia)

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, models.CASCADE)
    horario = models.TimeField()
    agendado = models.BooleanField(default=False)
    class Meta:
        unique_together = ('agenda', 'horario')

    def __str__(self):
        return str(self.horario)

class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)
    agenda = models.ForeignKey(Agenda, models.CASCADE)

    def __str__(self) -> str:
        return str(self.dia)
