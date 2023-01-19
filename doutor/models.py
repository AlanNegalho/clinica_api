from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError


class Especialidade(models.Model):
    nome = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=30)
    crm = models.CharField(max_length=30)
    email = models.EmailField( max_length=50,blank=True)
    telefone = models.CharField(max_length=30, verbose_name='Nº telefone celular')
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, verbose_name="Especialidade") #relacionamento 1-n
    #especialidade = models.ManyToManyField("Especialidade", verbose_name=("especialidade"))
    
    def __str__(self):
        return self.nome

def validate_day(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Porfavor escolha um dia útil da semana.')



class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico") 
    data = models.DateField(validators=[validate_day])
    
    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "13:00 ás 14:00"),
        ("5", "14:00 ás 15:00"),
    )
    horario = models.CharField(max_length=10, choices=Horarios, blank=False, null=False, default='1')

class Meta:
    unique_together = ('data', 'hora')

    def __str__(self):
        return f'{self.medico}: {self.data.strftime("%d/%b/%Y")} - {self.hora}'
