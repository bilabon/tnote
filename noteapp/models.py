from django.db import models

import datetime

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	text = models.TextField()
	date = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title
