from django.forms import ModelForm
from .models import *

class ForumForm(ModelForm):
	class Meta: 
		model = For_Post
		fields = '__all__' 