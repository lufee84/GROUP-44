from django.conf.urls import url
from city.views import HomeView

urlpatterns =[
    url(r'^$', HomeView.as_view(), name='home')

]