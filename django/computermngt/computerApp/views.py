from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from computerApp.models import Machine
from computerApp.models import PC
from computerApp.models import Personne

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines': machines}
    return render(request,'computerapp/machine_list.html',context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'computerapp/machine_detail.html', context)

def personnes_list_view(request) :
    personne = Personne.objects.all()
    context={'personneList': personne}
    return render(request,'computerapp/personne_list.html',context)

def personnes_detail_view(request, pk):
    personne = get_object_or_404(Personne, id=pk)
    context = {'personneDetail': personne}
    return render(request, 'computerapp/personne_detail.html', context)
