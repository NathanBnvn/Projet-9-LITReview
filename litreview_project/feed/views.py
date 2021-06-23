from itertools import chain
from django.shortcuts import render
from django.db.models import CharField, Value, Q
from django.contrib.auth.decorators import login_required
from .models import Review, Ticket, UserFollow
from .forms import TicketForm, ReviewForm

# Create your views here.


@login_required
def feed(request):
	review = Review.objects.filter(user=request.user)
	ticket = Ticket.objects.filter(user=request.user)

	#if ticket.exists(): 
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
def create_ticket(request):
	if request.method == 'POST':
		form = TicketForm(request.POST, request.FILES)
		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.user = request.user
			ticket.save()
	else:
		form = TicketForm()
	return render(request, 'feed/create_ticket.html', {'form': form})


@login_required
def create_review(request):
	if request.method == 'POST':
		review_form = TicketForm(request.POST)
		ticket_form = ReviewForm(request.POST, request.FILES)
		if review_form.is_valid() and ticket_form.is_valid() :
			review = review_form.save(commit=False)
			ticket = ticket_form.save(commit=False)
			review.user = request.user
			ticket.user = request.user
			
			review.ticket = ticket #il faut associé l'id de instance review.ticket au ticket 
			
			# les forms sont sujets à la casse, ils changent de place seules

			ticket.save()
			review.save()
	else:
		review_form = ReviewForm()
		ticket_form = TicketForm()	
	return render(request, 'feed/create_review.html', {'review_form': review_form, 'ticket_form': ticket_form })

