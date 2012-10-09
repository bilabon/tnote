from tnote.noteapp.models import Entry
from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    search_fields = ['title']
    date_hierarchy = 'date'

admin.site.register(Entry, EntryAdmin)
