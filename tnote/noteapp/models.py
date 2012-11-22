from django.db import models
import os
import random


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(random.randint(0, 1000000)), ext)
    return os.path.join('img', filename)


class Entry(models.Model):
    text = models.TextField()
    imagefile = models.ImageField(upload_to=get_file_path,
                                  verbose_name=u"Image",
                                  blank=True,
                                  null=True)

    def __unicode__(self):
        return self.text
