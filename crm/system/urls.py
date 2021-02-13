from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('debitoren/', views.alle_debitoren, name="alle_debitoren"),
    path('debitoren/neu', views.neuer_debitor, name="neuer_debitor"),
    path('debitoren/<str:pk>/', views.bearbeiten_debitor, name="bearbeiten_debitor"),
    path('kreditoren/', views.alle_kreditoren, name="alle_kreditoren"),
    path('kreditoren/neu', views.neuer_kreditor, name="neuer_kreditor"),
    path('kreditoren/<str:pk>/', views.bearbeiten_kreditor, name="bearbeiten_kreditor"),
    path('ausgangsrechnungen/', views.alle_ausgangsrechnungen, name="alle_ausgangsrechnungen"),
    path('ausgangsrechnung/<str:id>/', views.debitor_ausgangsrechnung, name="debitor_ausgangsrechnung"),
    path('ausgangsrechnung/<str:debitor>/neu/', views.debitor_neue_ausgangsrechnung, name="debitor_neue_ausgangsrechnung"),
    path('neue_ausgangsrechnung/', views.neue_ausgangsrechnung, name="neue_ausgangsrechnung"),
    path('eingangsrechnungen/', views.alle_eingangsrechnungen, name="alle_eingangsrechnungen"),
    path('eingangsrechnung/<str:id>/', views.kreditor_eingangsrechnung, name="kreditor_eingangsrechnung"),
    path('eingangsrechnung/<str:kreditor>/neu/', views.kreditor_neue_eingangsrechnung, name="kreditor_neue_eingangsrechnung"),
    path('neue_eingangsrechnung/', views.neue_eingangsrechnung, name="neue_eingangsrechnung"),
]
