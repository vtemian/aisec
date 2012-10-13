from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import settings

urlpatterns = patterns('',
    url(r'^$', 'common.views.base'),
    url(r'^user/login/', 'account.views.login'),
    url(r'^logout/?$',  'django.contrib.auth.views.logout_then_login'),
    url(r'^user/register/$',  'account.views.register'),
    url(r'^shop/buy/$',  'shop.views.buy'),
    url(r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),    url(r'^facebook/login$', 'facebook.views.login'),
    url(r'^facebook/authentication_callback$', 'facebook.views.authentication_callback'),
    url(r'^profile/(?P<profile_id>.*)/$', 'account.views.profile'),
    url(r'^404/$', 'common.views.handler404'),
)