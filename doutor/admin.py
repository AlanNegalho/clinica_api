from django.contrib import admin
from doutor.models import Especialidade, Medico, Agenda

# Register your models here.
@admin.register(Especialidade)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome','crm','telefone','email','especialidade')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('medico','data','horario')
    list_display_links = ('medico',)
    search_fields = ('medico',)
    list_per_page = 20

#admin.site.register(Especialidades, Especialidade)

# class Cursos(admin.ModelAdmin):
#     list_display = ('id', 'codigo_curso', 'descricao')
#     list_display_links = ('id', 'codigo_curso')
#     search_fields = ('codigo_curso',)
#     list_per_page = 20

# admin.site.register(Curso, Cursos)

# class Matriculas(admin.ModelAdmin):
#     list_display = ('id', 'aluno', 'curso')
#     list_display_links = ('id',)
#     list_per_page = 20

# admin.site.register(Matricula, Matriculas)
