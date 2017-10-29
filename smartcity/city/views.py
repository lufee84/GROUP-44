from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from city.forms import HomeForm
from city.models import Post


class HomePageView(TemplateView):
    template_name = "home/home.html"


class StudentPageView(TemplateView):
    template_name = "home/student.html"


class FeedbackView(TemplateView):
    template_name = 'home/feedback.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.all()

        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('city:feedback')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
