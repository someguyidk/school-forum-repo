from django.shortcuts import render
from pathlib import Path
from .models import *

polls_test = [
	{
	'id':'poll-1',
	'title':'First Poll',
	'question':'Are cats better than dogs?',
	'approval':70,
	},
	{
	'id':'poll-2',
	'title':'Second Poll',
	'question':'Should TOK be kept as a class?',
	'approval': 20,
	},
] 

def home(request):
	return render(request, 'forum/home.html')

def calendar(request):
	print(Path(__file__).resolve())
	return render(request, 'forum/calendar.html')

def polls(request):
	context = {'polls':polls_test}
	return render(request, 'forum/polls.html', context)

def create_forum(request):
	return render(request, 'forum/create_forum.html')

def forum(request):
	context = {'posts':For_Post.objects.all()}
	return render(request, 'forum/forum.html', context)

def profile(request):
	return render(request, 'forum/profile.html')

def create_forum(request):
	return render(request, 'forum/create_forum.html')