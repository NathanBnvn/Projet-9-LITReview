from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def feed(request):
	pass

@login_required
def create_review(request):
	pass

@login_required
def ask_review(request):
	pass