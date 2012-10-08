from django.db import models

import datetime

from django.core.validators import RegexValidator

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField( blank=True)
	text = models.TextField( validators=[RegexValidator(regex='^.{10,}?$', message='Length should be at least 10 characters!', code='nomatch')])
	date = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title
