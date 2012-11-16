from django.db import models
from django.core.validators import MinLengthValidator


class Entry(models.Model):
    text = models.TextField(validators=[MinLengthValidator(10)])

    def __unicode__(self):
        return self.text


class Imgfile(models.Model):
    imagefile = models.ImageField(upload_to='img', verbose_name=u"Image",
                                                                    blank=True)

    def __unicode__(self):
        return self.imagefile.path.split('/')[-1]
