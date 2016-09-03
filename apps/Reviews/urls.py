from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^books$', views.home),
	url(r'^books/add$', views.add),
	url(r'^books/(?P<item_id>\d+)$', views.show, name = 'my_show'),
	url(r'^users/(?P<user_id>\d+)$', views.user),
	url(r'^books/create$', views.create),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^review/(?P<item_id>\d+)$', views.review),
	url(r'^logout$', views.logout),
	url(r'^delete/(?P<item_id>\d+)$', views.delete),
]