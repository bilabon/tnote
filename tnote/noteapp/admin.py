from django.db import models
from django.contrib import admin
from tnote.noteapp.models import Entry
from tnote.noteapp.widgets import DynamicAmount


class EntryAdmin(admin.ModelAdmin):
    search_fields = ['text']

    formfield_overrides = {
        models.TextField: {'widget': DynamicAmount},
    }

admin.site.register(Entry, EntryAdmin)
