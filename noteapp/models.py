from django.db import models
import datetime
from django.core.validators import RegexValidator, MinLengthValidator


class Entry(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
