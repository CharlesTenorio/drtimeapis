# Generated by Django 3.0.1 on 2019-12-28 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinica_profissional', '0001_initial'),
        ('cliente', '0002_cliente_num_verificacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_agenda', models.CharField(choices=[('Marcado', 'Marcado'), ('Confirmado', 'Confiramdo'), ('Cancelado Cliente', 'Cancelado Cliente'), ('Cancelado Profissional', 'Cancelado Profissional'), ('Cancelado Clinica', 'Cancelado Clinica'), ('Em atendimento', 'Em atendimento'), ('Atendido', 'Atendido'), ('Remarcado', 'Remarcado')], max_length=30)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Cliente')),
                ('id_clinica_profi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica_profissional.ClinicaProfissional')),
            ],
        ),
    ]