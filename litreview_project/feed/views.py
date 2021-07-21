from itertools import chain
from django.shortcuts import render, redirect
from django.db.models import CharField, Value, Q
from django.contrib.auth.decorators import login_required
from profil.models import Book
from .models import Review, Ticket, UserFollow
from .forms import TicketForm, ReviewForm

# Create your views here.


def get_users_viewable_reviews(request):
    user_reviews = Review.objects.filter(user=request.user)
    followings = UserFollow.objects.filter(followed_user=request.user)
    for following in followings:
        following_user_reviews = Review.objects.filter(user=following.user)
        reviews = user_reviews | following_user_reviews
        return reviews


def get_users_viewable_tickets(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    followings = UserFollow.objects.filter(followed_user=request.user)
    for following in followings:
        following_user_tickets = Ticket.objects.filter(user=following.user)
        tickets = user_tickets | following_user_tickets
        return tickets


def get_responded_tickets(request):
    reviews = get_users_viewable_reviews(request)
    resolve_tickets_id = []
    tickets_id = []
    for review in reviews:
        resolve_tickets = Ticket.objects.filter(
            id=review.ticket.id
            ).values_list(
                'pk', flat=True
                )
        resolve_tickets_id.append(resolve_tickets)
    for ticket_id in resolve_tickets_id:
        tickets_id.append(ticket_id[0])
    return tickets_id


def get_wishlisted_reviews(request):
    books = Book.objects.filter(user=request.user)
    wishlisted_reviews_id = []
    for book in books:
        wishlisted_reviews_id.append(book.ticket_id)
    return wishlisted_reviews_id


@login_required
def feed(request):
    reviews = get_users_viewable_reviews(request)
    tickets = get_users_viewable_tickets(request)
    if tickets or reviews:
        reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
        tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
        resolve_tickets = get_responded_tickets(request)
        wishlisted_reviews = get_wishlisted_reviews(request)
        posts = sorted(
            chain(tickets, reviews),
            key=lambda post: post.time_created,
            reverse=True,
        )
        return render(
            request,
            "feed/feed.html",
            {
                "posts": posts,
                "resolve_tickets": resolve_tickets,
                "range": range(5),
                "wishlisted_reviews": wishlisted_reviews
            },
        )
    else:
        message = (
            "Il n'y a pas encore de critiques ou de tickets dans votre flux."
            )
        return render(
            request,
            "feed/feed.html",
            {
                "message": message,
            },
        )


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("feed")
    else:
        form = TicketForm()
    return render(request, "feed/create_ticket.html", {"form": form})


@login_required
def create_review(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        ticket_form = TicketForm(request.POST, request.FILES)
        if review_form.is_valid() and ticket_form.is_valid():
            review = review_form.save(commit=False)
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("feed")
    else:
        review_form = ReviewForm()
        ticket_form = TicketForm()
    return render(
        request,
        "feed/create_review.html",
        {"review_form": review_form, "ticket_form": ticket_form},
    )


@login_required
def respond_review(request, post_id):
    tickets = Ticket.objects.filter(id=post_id)
    print(tickets[0])
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = tickets[0]
            review.user = request.user
            review.save()
            return redirect("feed")
    else:
        form = ReviewForm()
    return render(
        request, "feed/resolve_review.html", {"form": form, "tickets": tickets}
    )
