from django.contrib import admin

from . import models


@admin.register(models.Panino)
class PaninoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Prenotazione)
class PrenotazioneAdmin(admin.ModelAdmin):
    pass
