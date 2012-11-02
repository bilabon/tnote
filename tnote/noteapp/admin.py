from django.db import models
from django.contrib import admin
from tnote.noteapp.models import Entry, Imgfile
from tnote.noteapp.widgets import DynamicAmountOfSymbols


class EntryAdmin(admin.ModelAdmin):
    search_fields = ['text']
    formfield_overrides = {
        models.TextField: {'widget': DynamicAmountOfSymbols()},
    }

admin.site.register(Imgfile)
admin.site.register(Entry, EntryAdmin)
