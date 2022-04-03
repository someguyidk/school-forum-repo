from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)
from pathlib import Path
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import render


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
	posts = For_Post.objects.all().order_by('-date_posted')
	paginator = Paginator(posts, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'posts':posts,'form':form, 'page_obj': page_obj}
	
	if request.method == 'POST':
		form = ForumForm(request.POST, request.FILES)
		form.instance.author = request.user
		print(form.instance.author)
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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = For_Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = For_Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def profile(request):
	return render(request, 'forum/profile.html')
