from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_posts, name='posts'),
	path('modifier/', views.update, name='update')
]