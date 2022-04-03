from django.forms import ModelForm
from .models import *

class ForumForm(ModelForm):
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		print("FORM VALID")

	class Meta: 
		model = For_Post
		fields = ['title','content', 'AN', 'file']