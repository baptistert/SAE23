# Generated by Django 4.0.4 on 2022-06-14 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('num_c', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=24)),
                ('nom', models.CharField(max_length=18)),
                ('prenom', models.CharField(max_length=18)),
                ('poste', models.CharField(choices=[('TECHNICIEN', 'TECHNICIEN'), ('ADMIN', 'ADMIN'), ('USER', 'USER - Poste')], default='TECHNICIEN', max_length=12)),
                ('addr_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('num_e', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('SWITCH', 'SWITCH'), ('ROUTEUR', 'ROUTEUR'), ('FIREWALL', 'FIREWALL')], default='SWITCH', max_length=12)),
                ('infra', models.CharField(max_length=32)),
                ('uti', models.CharField(max_length=12)),
                ('last_maj', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('num_i', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=12)),
                ('nb_mach', models.CharField(max_length=12)),
                ('nb_equi', models.CharField(max_length=24)),
                ('respon', models.CharField(max_length=18)),
                ('entretien', models.DateField()),
            ],
        ),
    ]
