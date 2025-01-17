# Generated by Django 5.1.3 on 2024-12-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_customuser_ejercicios_resueltos_ultimos_siete_dias_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='daily_exercises',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_solved_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='max_streak',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='streak_days',
        ),
        migrations.AddField(
            model_name='customuser',
            name='ejercicios_resueltos_ultimos_siete_dias',
            field=models.JSONField(default=list),
        ),
    ]
