# Generated by Django 3.0.1 on 2019-12-28 09:22

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('cep', models.CharField(max_length=10, verbose_name='CEP *')),
                ('logradouro', models.CharField(max_length=80, verbose_name='Logradouro *')),
                ('numero', models.CharField(max_length=5, verbose_name='Número *')),
                ('complemento', models.CharField(blank=True, max_length=30, null=True)),
                ('bairro', models.CharField(max_length=40, verbose_name='Bairro *')),
                ('localidade', models.CharField(max_length=50, verbose_name='Cidade *')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='PE', max_length=2, verbose_name='Estado *')),
                ('fone', models.CharField(max_length=15)),
                ('fone1', models.CharField(blank=True, max_length=15, null=True)),
                ('fone2', models.CharField(blank=True, max_length=15, null=True)),
                ('pontuacao', models.FloatField(default=0)),
                ('token', models.CharField(blank=True, default='ST', max_length=250, null=True)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('imagem', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Foto de Perfil')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('senha', models.CharField(max_length=150)),
                ('token_fcm', models.CharField(blank=True, max_length=250, null=True)),
                ('data_cad', models.DateTimeField(auto_now_add=True)),
                ('id_usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
    ]
