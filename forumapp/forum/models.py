from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Forum post db model
class For_Post(models.Model):
	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=150)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#When user (author) is deleted so is their posts
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#AN = "annonymous"
	AN = models.BooleanField(default=False)
	file = models.FileField()

	def __str__(self):
		return self.title
#So the db model for possibly maybe polls?

#class For_Polls(models.Model):
class For_Polls(models.Model):
	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=150)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#When user (author) is deleted so is their posts
	author = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):
		return self.title
