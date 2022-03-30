from django.urls import path
from . import views
from .views import *

urlpatterns= [
	path('', views.home, name='forum_home'),
	path('home/', views.home, name='forum_home'),
	path('calendar/', views.calendar, name='calendar'),
	path('polls/', views.polls, name='polls'),
	path('create_poll/',views.create_forum, name='create_poll'),
	path('forum/', views.forum, name="forum_forum"),
	#path('forum/', PostListView.as_view(), name="forum_forum"),
	path('forum/post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('forum/post/new/', PostCreateView.as_view(), name='post_create'),
	path('profile/',views.profile, name="profile"),
	path('create_forum/',views.create_forum, name="create_forum"),
]