# Generated by Django 3.0.2 on 2020-01-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_agendamento_id_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='data_cadstro',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
