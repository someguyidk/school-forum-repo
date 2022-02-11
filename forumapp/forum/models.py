from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Forum post db model
class For_Post(models.Model):
	title = models.CharField(max_length=150)
	#content
	#date_posted


#So the db model for possibly maybe polls?

#class For_Polls(models.Model):
#	options = list?
#	amount of oprtions = len(options)



