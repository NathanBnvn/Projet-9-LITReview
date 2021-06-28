from itertools import chain
from django.shortcuts import render
from django.db.models import CharField, Value, Q
from django.contrib.auth.decorators import login_required
from .models import Review, Ticket, UserFollow
from .forms import TicketForm, ReviewForm

# Create your views here.


@login_required
def feed(request):
	followings = UserFollow.objects.filter(followed_user=request.user)
	for following in followings:
		tickets = Ticket.objects.filter(user=following.user)
		tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
		reviews = Review.objects.filter(user=following.user)
		reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
		if tickets.exists() or reviews.exists(): 
			posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
			return render(request, 'feed/feed.html', {'posts': posts})
	else :
		message = "Il n'y a pas encore de critiques ou de tickets dans votre flux."
		return render(request, 'feed/feed.html', {'message': message})

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
		review_form = ReviewForm(request.POST)
		ticket_form = TicketForm(request.POST, request.FILES)
		if review_form.is_valid() and ticket_form.is_valid() :
			review = review_form.save(commit=False)
			ticket = ticket_form.save(commit=False)
			ticket.user = request.user
			ticket.save()
			review.user = request.user
			review.ticket = ticket
			review.save()
	else:
		review_form = ReviewForm()
		ticket_form = TicketForm()	
	return render(request, 'feed/create_review.html', {'review_form': review_form, 'ticket_form': ticket_form })

