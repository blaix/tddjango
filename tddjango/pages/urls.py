from django.conf.urls import patterns, url

from pages.views import PageView


urlpatterns = patterns('',
    url(r'(?P<page>.+)', PageView.as_view()),
)
