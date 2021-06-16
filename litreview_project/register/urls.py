from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
	path('', LoginView.as_view(), name='login'),
 	path('register/', views.register, name='register')
]