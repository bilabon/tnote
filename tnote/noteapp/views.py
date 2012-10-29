from django.views.generic.simple import direct_to_template
from django.shortcuts import render
from django.utils import simplejson
from django.http import HttpResponse
from django.conf import settings
import random

from tnote.noteapp.models import Entry, Imgfile
from tnote.noteapp.forms import AddForm, AddImage


def index(request):
    entries = Entry.objects.all()
    return direct_to_template(request, 'index.html', {'entries': entries, },)


def formadd(request):
    if (request.method == 'POST' and request.is_ajax()):
        if (request.FILES):
            n = str(random.randint(0, 100000))
            try:
                img_extension = request.FILES['imagefile'].name.split('.')[-1]
                request.FILES['imagefile'].name = u"%s.%s" % (n, img_extension)
            except:
                print 'Error image.'
        form = AddForm(request.POST)
        formimg = AddImage(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            response = u'Note has been sent.'
            return HttpResponse(simplejson.dumps({'response': response,
                                                  'result': 'success', }))
        elif (formimg.is_valid() and request.FILES):
            formimg.save()
            imagefileurl = formimg.save().imagefile.url
            response = u'Image been added.'
            response += u" Name: %s | Photo size: %s byte" % (
            request.FILES['imagefile'].name, request.FILES['imagefile'].size)
            return HttpResponse(simplejson.dumps({'response': response,
                                                  'imagefileurl': imagefileurl,
                                                  'result': 'success', }))
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            response2 = {}
            for kk in formimg.errors:
                response2[kk] = formimg.errors[kk][0]
            return HttpResponse(simplejson.dumps({'response': response,
                                                  'response2': response2,
                                                  'result': 'error',
                                                  'result2': 'error', }))
    form = AddForm()
    formimg = AddImage()
    return direct_to_template(request, "formadd.html",
                              extra_context={'form': form,
                                             'formimg': formimg, },)
