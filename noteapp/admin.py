from noteapp.models import Entry
from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text', 'date')
    search_fields = ['title']
    date_hierarchy = 'date'

admin.site.register(Entry, EntryAdmin)
