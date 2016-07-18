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
    url(r'^post/([a-zA-Z0-9\+\-_]+)/$', views.post, name='post'),
    url(r'^edit-post/([a-zA-Z0-9\+\-_]+)/$', views.edit_post, name='edit_post'),
    url(r'^new-post/$', views.new_post, name='new_post'),
    url(r'^delete-post/([a-zA-Z0-9\+\-_]+)/$', views.delete_post, name='delete_post'),
    url(r'^feed/$', PostFeed(), name='feed'),
    url(r'^category/([a-zA-Z0-9\+\-_]+)/$', views.category, name='category'),
    url(r'^tag/([a-zA-Z0-9\+\-_]+)/$', views.tag, name='tag'),
    url(r'^archive/(\d{4})/(\d{2})/$', views.archive, name='archive'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^change-profile/$', views.change_profile, name='change_profile'),
    url(r'^new_category/$', views.new_category, name='new_category'),
    url(r'^new_tag/$', views.new_tag, name='new_tag'),
]
