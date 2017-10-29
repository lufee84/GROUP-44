from django.conf.urls import url
from django.views.generic import TemplateView
from city.views import FeedbackView, HomePageView, StudentPageView

urlpatterns =[
    url(r'^$', HomePageView.as_view(template_name="home/home.html"), name='home'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^$', TemplateView.as_view(template_name="home/student.html"), name='student'),

]
