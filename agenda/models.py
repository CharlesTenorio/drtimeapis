from django.db import models
from clinica_profissional.models import ClinicaProfissional
from horario.models import HorarioAgenda
from cliente.models import Cliente
from django.conf import settings


class Agendamento(models.Model):
    id_clinica_profi = models.ForeignKey(ClinicaProfissional, on_delete=models.PROTECT)
    id_horario = models.ForeignKey(HorarioAgenda, on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    status_agenda = models.CharField(max_length=30, choices=settings.ST_AGENDA_CHOICES)
