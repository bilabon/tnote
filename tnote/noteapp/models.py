from django.db import models


class Entry(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text
