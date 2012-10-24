from django.views.generic.simple import direct_to_template
from django.shortcuts import render
from django.utils import simplejson
from django.http import HttpResponse

from tnote.noteapp.models import *
from tnote.noteapp.forms import *


def index(request):
    entries = Entry.objects.all()
    return direct_to_template(request, 'index.html', {'entries': entries},)


def formadd(request):
    if (request.method == 'POST' and request.is_ajax()):
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            response = "Note has been sent."
            return HttpResponse(simplejson.dumps({'response': response,
                                                  'result': 'success'}))
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse(simplejson.dumps({'response': response,
                                                  'result': 'error'}))
    form = AddForm()
    return direct_to_template(request, "formadd.html",
                                          extra_context={'form': form})
