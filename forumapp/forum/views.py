from django.shortcuts import render, redirect
from pathlib import Path
from .models import *
from .forms import *

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
	form = ForumForm()
	context = {'form':form}

	return render(request, 'forum/create_forum.html', context)

def forum(request):
	form = ForumForm()
	context = {'posts':For_Post.objects.all(),'form':form}
	form = ForumForm()
	
	if request.method == 'POST':
		form = ForumForm(request.POST, request.FILES)
		print(request.POST)

		if form.is_valid():
			form.save()
			return redirect('forum_forum')
	else:
		form = ForumForm()
	return render(request, 'forum/forum.html', context)

def profile(request):
	return render(request, 'forum/profile.html')
