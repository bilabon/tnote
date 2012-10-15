from django import template
from tnote.noteapp.models import *

register = template.Library()


@register.simple_tag
def render_one_text_note(number_id):
    try:
        t = Entry.objects.get(pk=number_id)
    except Entry.DoesNotExist:
        print "Error. Incorrect ID. Apress isn't in database yet."
        return ""
    else:
        return t.text
