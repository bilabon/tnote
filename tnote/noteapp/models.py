from django.db import models
from django.core.validators import MinLengthValidator


class Entry(models.Model):
    text = models.TextField(validators=[MinLengthValidator(10)])

    def __unicode__(self):
        return self.text
