from django.core.files import File
from django.views.decorators.http import require_POST
from tnote.noteapp.models import Imgfile
from tnote.noteapp.forms import UploadImage
import random


@require_POST
def upload_images(request):
    n = str(random.randint(0, 100000))
    try:
        img_extension = request.FILES['imagefile'].name.split('.')[-1]
        request.FILES['imagefile'].name = "%s.%s" % (n, img_extension)
    except:
        return None
    _form = UploadImage(request.POST, request.FILES)
    if request.method == 'POST' and _form.is_valid():
        imgurl = _form.save().imagefile.url
        return imgurl
    return None
