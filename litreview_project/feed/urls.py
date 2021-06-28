from django.urls import path
from . import views

urlpatterns = [
	path('', views.feed, name='feed',),
	path('creer-critique/', views.create_review, name='create-review'),
	path('repondre-ticket/<post_id>', views.respond_review, name='respond-review'),
	path('creer-ticket/', views.create_ticket, name='create-ticket')
]