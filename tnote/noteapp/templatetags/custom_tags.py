from django import template
register = template.Library()
from tnote.noteapp.models import *


@register.inclusion_tag('sh.html')
def render_all_text_note():
    entries = Entry.objects.all()
    return {'entries': entries}
