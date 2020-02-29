from rest_framework.generics import CreateAPIView, ListAPIView

from .. import models
from . import serializers


class PaninoListView(ListAPIView):
    queryset = models.Panino.objects.all()
    serializer_class = serializers.PaninoSerializer


class PrenotazioniCreateView(CreateAPIView):
    queryset = models.Prenotazione.objects.all()
    serializer_class = serializers.PrenotazioneWriteSerializer


class PrenotazioniListView(ListAPIView):
    queryset = models.Prenotazione.objects.all()
    serializer_class = serializers.PrenotazioneReadSerializer
