from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<guide_id>[0-9]+)/$', views.guide, name='guide'),
    url(r'^$', views.index, name='index'),
]
