from rest_framework import serializers

from .. import models


class PaninoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Panino
        fields = [
            "nome",
            "descrizione",
            "prezzo",
            "disponibilita",
        ]


class PrenotazioneReadSerializer(serializers.ModelSerializer):
    panini = PaninoSerializer(many=True)

    class Meta:
        model = models.Prenotazione
        fields = [
            "studente",
            "classe",
            "ritiro",
            "panini",
        ]


class PrenotazioneWriteSerializer(PrenotazioneReadSerializer):
    panini = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Panino.objects.all())
