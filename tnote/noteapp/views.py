from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.template import RequestContext

from tnote.noteapp.models import *
from tnote.noteapp.forms import *


def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})
