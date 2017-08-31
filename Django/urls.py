"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

Символ/выражение Совпадающая строка
. (Точка)           Любой символ
^ (Каретка)         Начало строки
$                   Конец строки
*                   0 или более повторений
+                   1 или более повторений
?                   0 или 1 повторение
|                   А | В означает A или B
[a-z]               Любые буквы в нижнем регистре
\w                  Любой цифробуквенный символ или _
\d                  Любая цифра

"""
from django.conf.urls import url
from django.contrib import admin

from DjangoApp import views
from DjangoApp.views import Index, Profile, PostPost

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name='home'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^user/(\w+)/post/$', PostPost.as_view())
]
