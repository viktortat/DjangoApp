from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .models import Post
from user_profile.models import User


def home(request):
    content = {'text': 'Привет мир!!!', 'title': 'Главная страница'}
    return render(request, 'base.html', content)


class Index(View):
    def get(self, request):
        content = {'text': 'Начало...', 'title': 'Главная страница'}
        return render(request, 'base.html', content)
        # return HttpResponse('Запрос на GET')

    def post(self, request):
        return HttpResponse('Запрос на POST')


class Profile(View):
    """ User Profile Page url: user/<username>"""
    def get(self, request, username):
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user=user)
        context = {
            'posts': posts,
            'user': user
        }
        return render(request, 'profile.html', context)
