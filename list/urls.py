from django.conf.urls import url
from list import views

# Regex url pattern
urlpatterns = [
    url(r'^games/$', views.game_list),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
]