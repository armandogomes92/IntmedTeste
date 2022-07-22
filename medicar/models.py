from django.db import models

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
    agenda = models.ForeignKey(Agenda, models.CASCADE, related_name='horarios')
    horario = models.TimeField()
    agendado = models.BooleanField(default=False)
    class Meta:
        unique_together = ('agenda', 'horario')

    def __str__(self):
        return str(self.horario)

class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, models.CASCADE)
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.dia)

