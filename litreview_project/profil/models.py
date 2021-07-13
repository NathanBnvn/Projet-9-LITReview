from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=128)
	author = models.CharField(max_length=128)
	summary = models.TextField(max_length=2048, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to="images/")
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ticket_id = models.IntegerField(blank=True)
	time_created = models.DateTimeField(auto_now_add=True)
