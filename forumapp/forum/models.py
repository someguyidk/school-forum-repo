from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Forum post db model
class For_Post(models.Model):
	id = models.AutoField(primary_key = True, blank=True)
	title = models.CharField(max_length=150)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now, blank=True)
	#When user (author) is deleted so is their posts
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#AN = "annonymous"
	AN = models.BooleanField(default=False)
	file = models.FileField(upload_to = 'user/files/', blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs = {'pk':self.pk})

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

 

