from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
)
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
	context = {'posts':For_Post.objects.all().order_by('-date_posted'),'form':form}
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

# Alt class based views for forum page
class PostListView(ListView):
	model = For_Post 
	template_name = 'forum/forum.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = For_Post 

	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = For_Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def profile(request):
	return render(request, 'forum/profile.html')
