from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def posts(request):
	return render(request, 'posts/posts.html')

@login_required
def update_review(request):
	return render(request, 'posts/update_review.html')

@login_required
def update_ticket(request):
	return render(request, 'posts/update_ticket.html')