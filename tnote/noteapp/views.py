from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.utils import simplejson

from tnote.noteapp.models import *
from tnote.noteapp.forms import *
import random


def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries},)


def formadd(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddForm()
            formimg = UploadImage()
            response = 'Note was successfully added.'
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'success'}))
            messages.success(request, response)
            return render(request, 'formadd.html', {'form': form,
                                                    'formimg': formimg},)
        else:
            response = 'Some error in your data.'
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'result': 'error'}))
            messages.error(request, response, {'form': form})
    else:
        form = AddForm()
    formimg = UploadImage()
    return render(request, 'formadd.html', {'form': form, 'formimg': formimg})


@require_POST
def upload_img(request):
    if (request.FILES):
        n = str(random.randint(0, 100000))
        resp_error = 'Some error with your Image.'
        try:
            img_extension = request.FILES['imagefile'].name.split('.')[-1]
            request.FILES['imagefile'].name = "%s.%s" % (n, img_extension)
        except:
            return HttpResponse(simplejson.dumps({'response': resp_error,
                                                      'result': 'error'}))
        formimg = UploadImage(request.POST, request.FILES)
        if formimg.is_valid():
            imgurl = formimg.save().imagefile.url
            response = 'Image was successfully attach.'
            return HttpResponse(simplejson.dumps({'response': response,
                                                  'imgurl': imgurl,
                                                  'result': 'success'}))
        else:
            return HttpResponse(simplejson.dumps({'response': resp_error,
                                                      'result': 'error'}))
