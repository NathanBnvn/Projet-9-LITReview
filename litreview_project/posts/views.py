from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from feed.models import Ticket, Review
import itertools as it

# Create your views here.

@login_required
def show_posts(request):
	reviews = Review.objects.filter(user=request.user)
	reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
	tickets = Ticket.objects.filter(user=request.user)
	tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
	posts = sorted(it.chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
	return render(request, 'posts/posts.html', {'posts':posts})

@login_required
def update(request):
	return render(request, 'posts/update_review.html')

@login_required
def erase(request, post_id):
	print(post_id)
	return redirect('posts')