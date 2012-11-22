from django import template
from tnote.noteapp.models import Entry

register = template.Library()


@register.simple_tag
def render_one_text_note(number_id):
    """
    Custom template tag that will render one text note
    by given id of note.
    """
    try:
        entry = Entry.objects.get(pk=number_id)
        return entry.text
    except Entry.DoesNotExist:
        return ""
