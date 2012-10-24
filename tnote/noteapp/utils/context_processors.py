from tnote.noteapp.models import Entry


def total_count_of_notes(request):
    e = Entry.objects.count()
    return {'total_count_of_notes': e, }
