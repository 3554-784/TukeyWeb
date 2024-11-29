# Generated by Django 5.1.3 on 2024-11-28 00:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('dificultad', models.CharField(choices=[('Básico', 'Básico'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado'), ('Experto', 'Experto')], max_length=20)),
                ('tiempo_estimado', models.DurationField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicios', to='exercises.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_completado', models.DateTimeField(auto_now_add=True)),
                ('intentos', models.IntegerField(default=0)),
                ('tasa_exito', models.FloatField(default=0.0)),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resoluciones', to='exercises.ejercicio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicios_resueltos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
