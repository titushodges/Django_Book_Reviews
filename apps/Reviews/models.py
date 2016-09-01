from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class books(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class reviews(models.Model):
	review = models.TextField()
	rating = models.CharField(max_length=255)
	user_id = models.ForeignKey(users, related_name='user_id', blank=True, null=True)
	book_id = models.ForeignKey(books, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

