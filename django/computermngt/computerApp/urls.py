from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipements/', views.equipement_list_view, name='equipements'),
    path('equipements/<pk>', views.equipement_detail_view, name='equipement-detail'),
    path('infrastructures/', views.infrastructure_list_view, name='infrastructures'),
    path('infrastructures/<pk>', views.infrastructure_detail_view, name='infrastructure-detail'),
    path('add-equipement/', views.equipement_add_form, name='add-equipement'),
    path('add-infrastructure/', views.infrastructure_add_form, name='add-infrastructure'),
    path('add-compte/', views.compte_add_form, name='add-compte'),
]