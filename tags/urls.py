__author__ = 'Vlad Temian'
from django.conf.urls.defaults import *

urlpatterns = patterns('tags.views',
    url(r'^search/$',  'search_tag'),
)

