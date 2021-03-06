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
	rating = models.IntegerField()
	user_id = models.ForeignKey(users, related_name='user_id', null=True, blank=True)
	book_id = models.ForeignKey(books, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

