from rest_framework import viewsets
from doutor.api import serializers
from doutor import models

class EspecialidadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EspecialidadeSerializer
    queryset = models.Especialidade.objects.all()

class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicoSerializer
    queryset = models.Medico.objects.all()

class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgendaSerializer
    queryset = models.Agenda.objects.all()