from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from feed.models import UserFollow

# Create your views here.

@login_required
def subscriptions(request):
	user = request.user
	# call user.following and user.followed_by
	fol = UserFollow.objects.select_related('user').get()	
	print(fol)
	search(request)
	return render(request, 'subscriptions/subscriptions.html')

def search(request):
	if request.method == 'POST':
		query = request.POST.get('search')
		requested_user = User.objects.filter(username__icontains=query)
		print(requested_user)
	#render(request, {'requested_user': requested_user})