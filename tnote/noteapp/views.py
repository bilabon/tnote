from django.shortcuts import render, get_list_or_404, get_object_or_404
import datetime
from tnote.noteapp.models import *


def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})


def renderbytag(request):
    return render(request, 'page_render_note_by_my_tag.html', {})
