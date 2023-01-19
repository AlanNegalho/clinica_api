from django.db import models
from doutor.models import Agenda

SEXO_CHOICES = (
    ('M','masculino'),
    ('F','feminino'),
)

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    email = models.EmailField( max_length=50,blank=True)
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES,null=True)
    telefone = models.CharField(max_length=30, verbose_name='Nº telefone celular')

    def __str__(self):
      return self.nome

class Consulta(models.Model):
    cliente  = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agenda_medico = models.OneToOneField(Agenda, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cliente', 'agenda_medico')

    def __str__(self):
        return self.cliente

