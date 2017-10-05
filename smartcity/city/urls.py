from django.conf.urls import url
from django.views.generic import TemplateView
from city.views import FeedbackView, HomePageView

urlpatterns =[
    url(r'^$', TemplateView.as_view(template_name="home/home.html"), name='home'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),

]
