from tnote.noteapp.models import Entry
from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    search_fields = ['text']

admin.site.register(Entry, EntryAdmin)
