from django.urls import path
from . import views


urlpatterns= [
	path('home/', views.home, name='forum_home'),
	path('calendar/', views.calendar, name='calendar'),
	path('polls/', views.polls, name='polls'),
	path('create_poll/',views.create_forum, name='create_poll'),
	path('forum/', views.forum, name="forum_forum"),
	path('profile/',views.profile, name="profile"),
	path('create_forum/',views.create_forum, name="create_forum"),
]