from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from feed.models import UserFollow

# Create your views here.

@login_required
def subscriptions(request):
	user_follow = UserFollow.objects.select_related('followed_user').all()
	#for subscriber in user_follow:
	#	followers = subscriber.followed_user
	#	followings = subscriber.user
	search(request)
	return render(request, 'subscriptions/subscriptions.html', {'user_follow':user_follow})

def search(request):
	if request.method == 'POST':
		query = request.POST.get('search')
		requested_users = User.objects.filter(username__icontains=query)
		print(requested_users)
		#return render(request, 'subscriptions/result.html', {'requested_users': requested_users})