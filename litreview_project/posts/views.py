from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def posts():
	pass

@login_required
def update_review():
	pass

@login_required
def update_ticket():
	pass