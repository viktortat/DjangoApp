from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

def home(request):
    content = {'text':'Привет мир!!!','title':'Главная страница'}
    return render(request,'base.html',content)

class Index(View):
    def get(self,request):
        content = {'text': 'Привет мир!', 'title': 'Главная страница'}
        return render(request, 'base.html', content)
        # return HttpResponse('Запрос на GET')

    def post(self, request):
        return HttpResponse('Запрос на POST')
