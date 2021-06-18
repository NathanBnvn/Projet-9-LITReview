from itertools import chain
from django.shortcuts import render
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from .models import Review, Ticket, UserFollow
from .forms import TicketForm, ReviewForm

# Create your views here.


@login_required
def feed(request):
	return render(request, 'feed/feed.html')
	#reviews = get_users_viewable_reviews(request.user)  
    # returns queryset of reviews
    #reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    #tickets = get_users_viewable_tickets(request.user) 
    # returns queryset of tickets
    #tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    #posts = sorted(
    #    chain(reviews, tickets), 
    #    key=lambda post: post.time_created, 
    #    reverse=True
    #)
    #return render(request, 'feed/feed.html', context={'posts': posts})

@login_required
def create_review(request):
	form = ReviewForm
	return render(request, 'feed/create_review.html', {'form': form})

@login_required
def create_ticket(request):
	form = TicketForm
	return render(request, 'feed/create_ticket.html', {'form': form})