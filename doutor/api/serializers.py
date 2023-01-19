from rest_framework import serializers
from doutor import models
from datetime import date
from doutor.models import Agenda

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidade
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medico
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agenda
        fields = ('medico','data','horario')


    

        
    # def clean(self):
    #     super(AgendaSerializer, self).clean()

    #     data = self.cleaned_data.get('data')
    #     data_hj = date.today()

    #     if data < data_hj:
    #         self.errors['data'] = self.error_class(['Não é possível selecionar uma data já passada!'])

    #     medico = self.cleaned_data.get('medico')
    #     agenda_medico = Agenda.objects.filter(medico__id = medico.id)
        
    #     for agenda in agenda_medico:
    #         if data == agenda.data:
    #             self.errors['data'] = self.error_class(['Não é possível criar duas agendas na mesma data para um unico médico!'])           
    #             break          

    #     return self.cleaned_data