from django.urls import path
from . import views


urlpatterns= [
	path('forum/', views.home, name='forum-home'),
	path('calendar/', views.calendar, name='calendar'),
]