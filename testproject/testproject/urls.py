from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^', include('bambu_api.urls')),
)