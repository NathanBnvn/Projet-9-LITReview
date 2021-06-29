from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from feed.models import Ticket, Review
from feed.forms import TicketForm, ReviewForm
from itertools import chain

# Create your views here.

@login_required
def show_posts(request):
	reviews = Review.objects.filter(user=request.user)
	reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
	tickets = Ticket.objects.filter(user=request.user)
	tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
	posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
	return render(request, 'posts/posts.html', {'posts':posts})

@login_required
def update_ticket(request, post_id):
	review_view = False
	ticket = Ticket.objects.get(pk=post_id)
	form = TicketForm(request.POST or None, request.FILES or None, instance=ticket)
	if form.is_valid():
		form.save()
		return redirect('posts')
	return render(request, 'posts/update.html', {'form':form, 'review_view':review_view })

@login_required
def update_review(request, post_id):
	review = Review.objects.get(pk=post_id)
	ticket = review.ticket 
	review_view = True
	form = ReviewForm(request.POST or None, instance=review)
	if form.is_valid():
		form.save()
		return redirect('posts')
	return render(request, 'posts/update.html', {'form':form, 'ticket':ticket, 'review_view':review_view })

@login_required
def erase_ticket(request, post_id):
	ticket = Ticket.objects.get(pk=post_id)
	ticket.delete()
	return redirect('posts')

@login_required
def erase_review(request, post_id):
	review = Review.objects.get(pk=post_id)
	review.delete()
	return redirect('posts')