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
            name='Profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')], max_length=10)),
                ('login_social', models.CharField(blank=True, max_length=80, null=True)),
                ('fone', models.CharField(max_length=15, unique=True)),
                ('pontuacao', models.FloatField(default=0)),
                ('token', models.CharField(blank=True, default='ST', max_length=250, null=True)),
                ('cpf', models.CharField(max_length=14)),
                ('cosenho', models.CharField(max_length=30)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('imagem', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Foto de Perfil')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('senha', models.CharField(max_length=150)),
                ('confirma_sms', models.BooleanField(default=False)),
                ('token_fcm', models.CharField(blank=True, max_length=250, null=True)),
                ('mini_curriculum', models.TextField(blank=True, max_length=1000, null=True)),
                ('id_usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
    ]
