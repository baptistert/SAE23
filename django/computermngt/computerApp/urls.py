from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('personnes/', views.personnes_list_view, name='personnes'),
    path('personne/<pk>', views.personnes_detail_view, name='personne-detail'),
]