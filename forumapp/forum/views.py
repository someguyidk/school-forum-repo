from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
# Create your views here.

def home(request):
	return render(request, 'forum/home.html')

def calendar(request):
	print(Path(__file__).resolve())
	return render(request, 'forum/calendar.html')