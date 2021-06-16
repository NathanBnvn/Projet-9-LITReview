from django.urls import path
from . import views

urlpatterns = [
	path('', views.posts, name='posts'),
	path('modifier-critique/', views.update_review, name='update_review'),
	path('changer-ticket/', views.update_ticket, name='update_ticket')
]