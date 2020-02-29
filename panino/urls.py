from django.urls import path

from .api import views

urlpatterns = [
    path("panini/", views.PaninoListView.as_view(), name="panino-list"),
    path("prenotazioni/", views.PrenotazioniListView.as_view(), name="prenotazione-list"),
    path("prenotazione/", views.PrenotazioniCreateView.as_view(), name="prenotazione-create"),
]
