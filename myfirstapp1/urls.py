from django.conf.urls import patterns, url

from myfirstapp1 import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^upcoming-broadcasts/$', views.broadcasts, name='upcoming_broadcasts'),
    url(r'^broadcasts/selected-broadcast/$', views.selected_broadcast, name='selected_broadcast'),
    url(r'^sports$', views.sports, name='sports'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/selected-team/$', views.selected_team, name='selected_team'),
)
