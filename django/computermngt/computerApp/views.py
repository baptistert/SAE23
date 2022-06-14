from django.shortcuts import get_object_or_404
from computerApp.models import Equipement
from computerApp.models import Infrastructure
from computerApp.models import Compte
from .forms import AddCompteForm
from .forms import AddEquipementForm
from .forms import AddInfrastructureForm
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def index(request):
    context = {}
    return render(request, 'template/index.html', context)

def equipement_list_view(request) :
    equipements = Equipement.objects.all()
    context={'equipements': equipements}
    return render(request,'template/computerapp/equipement_list.html', context)

def equipement_detail_view(request, pk):
    equipement = get_object_or_404(Equipement, id=pk)
    context = {'equipement': equipement}
    return render(request, 'template/computerapp/equipement_detail.html', context)

def infrastructure_list_view(request) :
    infrastructures = Infrastructure.objects.all()
    context={'infrastructures': infrastructures}
    return render(request,'template/computerapp/infrastructure_list.html', context)

def infrastructure_detail_view(request, pk):
    infrastructure = get_object_or_404(Infrastructure, id=pk)
    context = {'infrastructure': infrastructure}
    return render(request, 'template/computerapp/infrastructure_detail.html', context)

def equipement_add_form(request):
    if request.method == 'POST':
        form = AddEquipementForm(request.POST or None)
        if form.is_valid():
            new_equi = Equipement(type=form.cleaned_data['type'], 
                                infra=form.cleaned_data['infra'], 
                                ip=form.cleaned_data['ip'], 
                                uti=form.cleaned_data['uti'],
                                last_maj=form.cleaned_data['addr_mail']
                                )
            new_equi.save()
            return redirect('equipements')
    else:
        form = AddEquipementForm()
        context = {'form': form}
        return render(request, 'template/computerapp/equipement_add.html', context)


def infrastructure_add_form(request):
    if request.method == 'POST':
        form = AddInfrastructureForm(request.POST or None)
        if form.is_valid():
            new_infra = Infrastructure(nom=form.cleaned_data['nom'], 
                                nb_mach=form.cleaned_data['nb_mach'], 
                                nb_equi=form.cleaned_data['nb_equi'], 
                                respon=form.cleaned_data['respon'],
                                entretien=form.cleaned_data['entretien']
                                )                    
            new_infra.save()
            return redirect('infrastructures')
    else:
        form = AddInfrastructureForm()
        context = {'form': form}
        return render(request, 'template/computerapp/infrastructure_add.html', context)


def compte_add_form(request):
    if request.method == 'POST':
        form = AddCompteForm(request.POST or None)
        if form.is_valid():
            new_compte = Compte(username=form.cleaned_data['username'], 
                                password=form.cleaned_data['password'], 
                                nom=form.cleaned_data['nom'], 
                                prenom=form.cleaned_data['prenom'],
                                poste=form.cleaned_data['addr_mail'],
                                addr_mail=form.cleaned_data['username']
                                )
            new_compte.save()
            return redirect('index')
    else:
        form = AddCompteForm()
        context = {'form': form}
        return render(request, 'template/computerapp/compte_add.html', context)