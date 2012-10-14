from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import RedirectView
from common.views import HomeView

admin.autodiscover()
import settings

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='discussion/discussions/default/inbox'), name='home'),
    url(r'^accounts/login/', 'account.views.login'),
    url(r'^accounts/logout/?$',  'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^user/register/$',  'account.views.register'),
    url(r'^discussion/', include('discussion.urls')),
    url(r'^tag/', include('tags.urls')),
    url(r'^notifications/', include('notification.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^profiles/', include('profiles.urls')),
)
