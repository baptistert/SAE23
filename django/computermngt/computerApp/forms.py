from django import forms
from django.core.exceptions import ValidationError


class AddCompteForm(forms.Form):
    username = forms.CharField(required=True, label='Nom d utilisateur', max_length=12)
    password = forms.CharField(required=True, label='Mot de passe', max_length=24)
    nom = forms.CharField(required=True, label='Nom', max_length=18)
    prenom = forms.CharField(required=True, label='Prenom', max_length=18)
    poste = forms.CharField(required=True, label='Poste', max_length=12)
    addr_mail = forms.EmailField(required=True, label='prenom.nom@rt-dev.com')

    def clean_username(self):
        data = self.cleaned_data["username"]
        if len(data) != 12:
            raise ValidationError("Erreur de format")
        return data

    def clean_password(self):
        data = self.cleaned_data["password"]
        if len(data) != 24:
            raise ValidationError("Erreur de format")
        return data

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 18:
            raise ValidationError("Erreur de format")
        return data

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) != 18:
            raise ValidationError("Erreur de format")
        return data

    def clean_poste(self):
        data = self.cleaned_data["poste"]
        if len(data) != 12:
            raise ValidationError("Erreur de format")
        return data

    def clean_addr_mail(self):
        data = self.cleaned_data["addr_mail"]
        if type(data) != forms.EmailField:
            raise ValidationError("Erreur de format")
        return data



class AddInfrastructureForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=18)
    nb_mach = forms.CharField(label='Prenom', max_length=3)
    nb_equi = forms.CharField(label='Poste', max_length=2)
    respon = forms.CharField(label='Responsable', max_length=18)
    entretien = forms.DateField(label='Date Maintenance')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 18:
            raise ValidationError("Erreur de format")
        return data

    def clean_nb_mach(self):
        data = self.cleaned_data["nb_mach"]
        if len(data) != 3:
            raise ValidationError("Erreur de format")
        return data

    def clean_nb_equi(self):
        data = self.cleaned_data["nb_equi"]
        if len(data) != 2:
            raise ValidationError("Erreur de format")
        return data

    def clean_respon(self):
        data = self.cleaned_data["respon"]
        if len(data) != 18:
            raise ValidationError("Erreur de format")
        return data

    def clean_entretien(self):
        data = self.cleaned_data["entretien"]
        if type(data) != forms.DateField:
            raise ValidationError("Erreur de format")
        return data



class AddEquipementForm(forms.Form):
    type = forms.CharField(label='Type', max_length=12)
    infra = forms.CharField(label='Infrastructure', max_length=24)
    ip = forms.CharField(label='IP', max_length=18)
    uti = forms.CharField(label='Utilisateur', max_length=18)
    last_maj = forms.DateField(label='Date MAJ')

    def clean_type(self):
        data = self.cleaned_data["type"]
        if len(data) != 12:
            raise ValidationError("Erreur de format")
        return data

    def clean_infra(self):
        data = self.cleaned_data["infra"]
        if len(data) != 24:
            raise ValidationError("Erreur de format")
        return data

    def clean_ip(self):
        data = self.cleaned_data["ip"]
        if len(data) != 18:
            raise ValidationError("Erreur de format")
        return data

    def clean_uti(self):
        data = self.cleaned_data["uti"]
        if len(data) != 18:
            raise ValidationError("Erreur de format")
        return data

    def clean_last_maj(self):
        data = self.cleaned_data["last_maj"]
        if type(data) != forms.DateField:
            raise ValidationError("Erreur de format")
        return data