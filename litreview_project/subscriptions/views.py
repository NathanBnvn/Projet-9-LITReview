from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from feed.models import UserFollow, Ticket, Review

# Create your views here.

@login_required
def subscriptions(request):
	search(request)
	followers = UserFollow.objects.filter(user=request.user)
	followings = UserFollow.objects.filter(followed_user=request.user)
	return render(request, 'subscriptions/subscriptions.html', {'followers': followers, 'followings':followings})

def search(request):
	if request.method == 'POST':
		query = request.POST.get('search')
		requested_users = User.objects.filter(username__icontains=query)
		# if requested_users.exists():
		# 	for user in requested_users:
		# 		ticket = Ticket.objects.filter(user=user).count() # il faut boucler pour avoir les utilisateurs un à un
		# 		review = Review.objects.filter(user=user).count() # et envoyer les résultats stockés. Le 0 n'est pas optimale
		# 	users = zip(requested_users, reviews, tickets)
		# 	print(user)
		return render(request, 'subscriptions/result.html', {'requested_users': requested_users})