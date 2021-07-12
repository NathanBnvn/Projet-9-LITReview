from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from feed.models import UserFollow, Ticket, Review
import itertools as it

# Create your views here.


@login_required
def subscriptions(request):
    search(request)
    followers = UserFollow.objects.filter(user=request.user)
    followings = UserFollow.objects.filter(followed_user=request.user)
    return render(
        request,
        "subscriptions/subscriptions.html",
        {"followers": followers, "followings": followings},
    )


@login_required
def search(request):
    if request.method == "POST":
        query = request.POST.get("search")
        requested_users = User.objects.filter(username__icontains=query).exclude(
            username=request.user
        )
        if requested_users.exists():
            tickets_count = [
                Ticket.objects.filter(user=user).count() for user in requested_users
            ]
            reviews_count = [
                Review.objects.filter(user=user).count() for user in requested_users
            ]
            following = [
                UserFollow.objects.filter(followed_user=request.user).filter(user=user)
                for user in requested_users
            ]
            requested_data = list(
                zip(requested_users, tickets_count, reviews_count, following)
            )
            return render(
                request, "subscriptions/result.html", {"requested_data": requested_data}
            )
        else:
            message = "Personne ne correspond à votre recherche"
            return render(request, "subscriptions/result.html", {"message": message})


@login_required
def subscribe(request, user):
    selected_user = User.objects.get(username=user)
    new_following = UserFollow(user=selected_user, followed_user=request.user)
    new_following.save()
    return redirect("subscriptions")


@login_required
def unsubscribe(request, follow_id):
    following = UserFollow.objects.get(pk=follow_id)
    following.delete()
    return redirect("subscriptions")
