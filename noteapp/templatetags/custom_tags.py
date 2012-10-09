from django import template

register = template.Library()

from noteapp.models import *


@register.simple_tag
def render_one_text_note(number_id):
    try:
        t = Entry.objects.get(pk=number_id)
    except Entry.DoesNotExist:
        print "Error. Incorrect ID. Apress isn't in the database yet."
        return ""
    else:
        return t.text.replace('\n', '</br>')
