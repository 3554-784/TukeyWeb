# Generated by Django 5.1.3 on 2024-11-30 23:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
        ('solutions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='submitted_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='status',
        ),
        migrations.AlterField(
            model_name='solution',
            name='language',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='problems.problem'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to=settings.AUTH_USER_MODEL),
        ),
    ]