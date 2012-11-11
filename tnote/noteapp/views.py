from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.utils import simplejson

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
            form = AddForm()
            response = 'Note was successfully added.'
            if request.is_ajax():
                print request.is_ajax()
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'success'}))
            messages.success(request, response)
            return render(request, 'formadd.html', {'form': form},)
        else:
            response = 'Some error in your data.'
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'error'}))
            messages.error(request, 'Some error in your data.')
    else:
        form = AddForm()
    return render(request, 'formadd.html', {'form': form},)
