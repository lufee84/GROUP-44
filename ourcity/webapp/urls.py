from django.conf.urls import url
from . import views

urlpatterns = [
    # /webapp/
    url(r'^$', views.index, name='index'),

    # /webapp/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
