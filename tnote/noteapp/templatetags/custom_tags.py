from django import template
from tnote.noteapp.models import *

register = template.Library()


@register.inclusion_tag('sh.html')
def render_all_text_note():
    entries = Entry.objects.all()
    return {'entries': entries}
