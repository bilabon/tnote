from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.template import RequestContext

from tnote.noteapp.models import *
from tnote.noteapp.forms import *


def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries},)


def formadd(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add/')
    else:
        form = AddForm()
    return render(request, 'formadd.html', {'form': form},)
