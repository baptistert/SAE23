from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from computerApp.models import Equipement
from computerApp.models import Infrastructure

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def equipement_list_view(request) :
    equipement = Equipement.objects.all()
    context={'equipementList': equipement}
    return render(request,'templates/computerapp/equipement_list.html',context)

def equipement_detail_view(request, pk):
    equipement = get_object_or_404(Equipement, id=pk)
    context = {'equipementDetail': equipement}
    return render(request, 'templates/computerapp/equipement_detail.html', context)

def infrastructure_list_view(request) :
    infrastructure = Infrastructure.objects.all()
    context={'infrastructureList': infrastructure}
    return render(request,'templates/computerapp/infrastructure_list.html',context)

def infrastructure_detail_view(request, pk):
    infrastructure = get_object_or_404(Infrastructure, id=pk)
    context = {'infrastructureDetail': infrastructure}
    return render(request, 'templates/computerapp/infrastructure_detail.html', context)
