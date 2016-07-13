from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from . import views
from .feeds import PostFeed
from .sitemaps import StaticSitemap, PostSitemap

sitemaps = {
    'static': StaticSitemap,
    'posts': PostSitemap,
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^post/(\d+)/$', views.post, name='post'),
    url(r'^post/(\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(\d+)/delete/$', views.delete_post, name='delete_post'),
    url(r'^post/feed/$', PostFeed(), name='feed'),
    url(r'^category/([a-zA-Z0-9\+\-_]+)/$', views.category, name='category'),
    url(r'^tag/([a-zA-Z0-9\+\-_]+)/$', views.tag, name='tag'),
    url(r'^archive/(\d{4})/(\d{2})/$', views.archive, name='archive'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/change/$', views.change_profile, name='change_profile'),
]
