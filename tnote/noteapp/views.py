from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.utils import simplejson

from tnote.noteapp.models import *
from tnote.noteapp.forms import *
from .noteapp_utils import upload_images


def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries},)


def formadd(request):
    if request.method == 'POST':
        if (request.FILES):
            files = upload_images(request)
            if files is not None:
                response = 'Image was successfully attach.'
                return HttpResponse(simplejson.dumps({'response': response,
                                                      'imgurl': files,
                                                      'result': 'success'}))
            else:
                resp_error = 'Some error with your Image.'
                return HttpResponse(simplejson.dumps({'response': resp_error,
                                                          'result': 'error'}))
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
