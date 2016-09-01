from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^books$', views.home),
	url(r'^books/add$', views.add),
	url(r'^books/(?P<item_id>\d+)$', views.show),
	url(r'^users/(?P<item_id>\d+)$', views.users),
	url(r'^books/create$', views.create),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^review$', views.review),
]