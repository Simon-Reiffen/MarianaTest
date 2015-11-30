from __future__ import unicode_literals

from django.db import models


class fizzbuzz(models.Model):
	useragent = models.TextField(default = " ") #stores data about who created the fizzbuzz
	
	created = models.DateField(auto_now_add=True) #keeps track of when the fizzbuzz was created

	message = models.TextField() #stores a string
	

	class Meta:
			ordering = ('created',)