from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from .feeds import PostFeed

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^post/(\d+)/$', views.post, name='post'),
    url(r'^post/(\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(\d+)/delete/$', views.delete_post, name='delete_post'),
    url(r'^post/feed/$', PostFeed(), name='feed'),
    url(r'^tag/(\w+)/$', views.tag, name='tag'),
    url(r'^archive/(\d{4})/(\d{2})/$', views.archive, name='archive'),
]
