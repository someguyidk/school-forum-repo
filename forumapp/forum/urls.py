from django.urls import path
from . import views


urlpatterns= [
	path('forum/', views.home, name='forum-home'),
	path('calendar/', views.calendar, name='calendar'),
	path('polls/', views.polls, name='polls'),
	path('create_poll/',views.create_forum, name='create-poll'),
]