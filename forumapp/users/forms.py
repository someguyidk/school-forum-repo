#:D
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from django.shortcuts import render, redirect
from .models import Profile

class UserRegistrationForm(UserCreationForm):
	email = EmailField(max_length = 100)
	def clean_email(self):
		email = self.cleaned_data['email']

		if email.split("@")[1].split(".")[0] != "eton" or email.split("@")[1].split(".")[1] != "edu" or email.split("@")[1].split(".")[2] != "mx":
			raise forms.ValidationError("Email does not pertain to eton domain")
		elif User.objects.filter(email=email).exists():
				raise forms.ValidationError("Email already in use")
		return email
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email = EmailField(max_length = 100)

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['image']




