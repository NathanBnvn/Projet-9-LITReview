from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feed.models import Ticket, Review
import itertools as it

# Create your views here.

@login_required
def show_posts(request):
	reviews = Review.objects.filter(user=request.user)
	tickets = Ticket.objects.filter(user=request.user)
	posts = sorted(it.chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
	return render(request, 'posts/posts.html', {'posts':posts})

@login_required
def update(request):
	return render(request, 'posts/update_review.html')