# Generated by Django 4.2.3 on 2023-08-03 03:12

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
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('aftas', models.BooleanField(default=False)),
                ('hipersensibilidade', models.BooleanField(default=False)),
                ('lesoes', models.BooleanField(default=False)),
                ('pos_cirurgia', models.BooleanField(default=False)),
                ('nevralgia', models.BooleanField(default=False)),
                ('consulta', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]