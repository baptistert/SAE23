from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/computerapp/equipement_list.html', views.equipement_list_view, name='equipement'),
    path('templates/computerapp/equipement_detail.html', views.equipement_detail_view, name='equipement-detail'),
    path('templates/computerapp/infrastructure_list.html', views.infrastructure_list_view, name='infrastructure'),
    path('templates/computerapp/infrastructure_detail.html', views.infrastructure_detail_view, name='infrasctructure-detail'),
]