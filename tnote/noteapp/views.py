from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.utils import simplejson

from urllib import quote
from django.db.models import Max
from math import ceil
import random

from tnote.noteapp.models import *
from tnote.noteapp.forms import *


def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries}, )


def formadd(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response = 'Note was successfully added.'
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'success'}))
            form = AddForm()
            messages.success(request, response)
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'error'}))
            messages.error(request, 'Some error in your data.')
    else:
        form = AddForm()
    return render(request, 'formadd.html', {'form': form}, )


def get_random_item(model, max_id=None):
    if max_id is None:
        max_id = model.objects.aggregate(Max('id')).values()[0]
    min_id = ceil(max_id * random.random())
    return model.objects.filter(id__gte=min_id)[0]


def randomnote(request):
    entries = get_random_item(Entry)
    e = quote(entries.text.replace('\r', '<br/>').encode("utf-8"))
    return HttpResponse('document.write(unescape("' + e + '"));',
                                                    mimetype="text/javascript")


def asite(request):
    url = 'http://' + request.META['HTTP_HOST'] + '/randomnote/'
    copy_string = '<script src="' + url + '" type="text/javascript"></script>'
    return render(request, 'asite.html', {'copy_string': copy_string}, )
