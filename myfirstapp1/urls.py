from django.conf.urls import patterns, url

from myfirstapp1 import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^games$', views.games, name='games'),
    url(r'^games/selected-game/$', views.selected_game, name='selected_game'),
                       
)
