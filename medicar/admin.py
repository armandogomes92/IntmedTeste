from django.contrib import admin

from medicar.models import Agenda, Horario, Medico

class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'crm')
    list_per_page = 20

class Agendas(admin.ModelAdmin):
    list_display = ('id', 'medico', 'dia')
    list_display_links = ('id', 'medico')
    list_per_page = 20 

admin.site.register(Medico, Medicos)

admin.site.register(Agenda, Agendas)

admin.site.register(Horario)