from curses import delay_output
from ssl import DefaultVerifyPaths
from django.db import models


# Create your models here.

class Compte(models.Model):

    TYPE = (
        ('TECHNICIEN', ('TECHNICIEN')),
        ('ADMIN', ('ADMIN')),
        ('USER', ('USER - Poste')),
    )

    num_c = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=24)
    nom = models.CharField(max_length=18)
    prenom = models.CharField(max_length=18)
    poste = models.CharField(max_length=12, choices=TYPE, default='TECHNICIEN')
    addr_mail = models.EmailField()



class Infrastructure(models.Model):

    num_i = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=12)
    nb_mach = models.CharField(max_length=12)
    nb_equi = models.CharField(max_length=24)
    respon = models.CharField(max_length=18)
    entretien = models.DateField()



class Equipement(models.Model):

    TYPE = (
        ('SWITCH', ('SWITCH')),
        ('ROUTEUR', ('ROUTEUR')),
        ('FIREWALL', ('FIREWALL')),
    )

    num_e = models.AutoField(primary_key=True, editable=False)
    type = models.CharField(max_length=12, choices=TYPE, default='SWITCH')
    infra = models.CharField(max_length=32)
    uti = models.CharField(max_length=12)
    last_maj = models.DateField()
