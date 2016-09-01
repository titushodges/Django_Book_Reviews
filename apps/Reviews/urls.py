from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^show/(?P<item_id>\d+)$', views.show),
	url(r'^new$', views.new),
	url(r'^edit/(?P<item_id>\d+)$', views.edit),
	url(r'^create$', views.create),
	url(r'^update/(?P<item_id>\d+)$', views.update),
	url(r'^destroy/(?P<item_id>\d+)$', views.destroy),
]