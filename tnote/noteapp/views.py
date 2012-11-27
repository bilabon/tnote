"""
Views of application noteapp.
"""

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.utils import simplejson

from urllib import quote
from django.db.models import Max
from math import ceil
import random
from django.core.urlresolvers import reverse

from tnote.noteapp.models import Entry
from tnote.noteapp.forms import AddForm


def get_widget_line(http_host, link):
    """
    Return a line of widget that can be inserted in any page.
    """
    url = 'http://%s%s' % (http_host, link)
    line = '<script src="' + url + '" type="text/javascript"></script>'
    return line


def index(request):
    """
    Main page of blog.
    """
    entries = Entry.objects.all()
    copy_string = get_widget_line(request.META['HTTP_HOST'],
                                  reverse('randomnote'))
    return render(request, 'index.html', {'entries': entries,
                                          'copy_string': copy_string}, )


def formadd(request):
    """
    Page for adding new articles and attach images.
    """
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response = 'Note was successfully added.'
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'success'},))
            form = AddForm()
            messages.success(request, response)
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'error'},))
    else:
        form = AddForm()
    return render(request, 'formadd.html', {'form': form}, )


def get_random_item(model, max_id=None):
    """
    Return random note from base.
    """
    if max_id is None:
        max_id = model.objects.aggregate(Max('id')).values()[0]
    min_id = ceil(max_id * random.random())
    return model.objects.filter(id__gte=min_id)[0]


def randomnote(request):
    """
    Page for widget that return random note.
    """
    entries = get_random_item(Entry)
    note = quote(entries.text.replace('\r', '<br/>').encode("utf-8"))
    out = 'document.write(decodeURIComponent("%s"));' % note
    return HttpResponse(out, mimetype="text/javascript")


def asite(request):
    """
    Page to show work widget that show random note.
    """
    copy_string = get_widget_line(request.META['HTTP_HOST'],
                                  reverse('randomnote'))
    return render(request, 'asite.html', {'copy_string': copy_string}, )
