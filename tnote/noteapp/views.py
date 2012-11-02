from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
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
            messages.success(request, 'Note has been sent.')
            return HttpResponseRedirect('/add/')
        else:
            messages.error(request, 'Error!')
    else:
        form = AddForm()
    return render(request, 'formadd.html', {'form': form},)
