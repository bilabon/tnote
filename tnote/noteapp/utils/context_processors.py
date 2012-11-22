from tnote.noteapp.models import Entry


def total_count_of_notes(request):
    """
    Custom context processor which pass amount of notes to templates.
    """
    entry = Entry.objects.count()
    return {'total_count_of_notes': entry, }
