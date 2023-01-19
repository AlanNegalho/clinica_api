# Generated by Django 4.1.4 on 2023-01-19 22:13

from django.db import migrations, models
import django.db.models.deletion
import doutor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('crm', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('telefone', models.CharField(max_length=30, verbose_name='Nº telefone celular')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doutor.especialidade', verbose_name='Especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(validators=[doutor.models.validate_day])),
                ('horario', models.CharField(choices=[('1', '08:00 ás 09:00'), ('2', '09:00 ás 10:00'), ('3', '10:00 ás 11:00'), ('4', '13:00 ás 14:00'), ('5', '14:00 ás 15:00')], default='1', max_length=10)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doutor.medico', verbose_name='Medico')),
            ],
        ),
    ]
