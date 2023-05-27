"""class_based_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from handle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',views.myview),
    path('fun/',views.MyView.as_view(name='ahsan_tariq')),
    path('funct/',views.MychildView.as_view()),
    path('view/',views.renderv),
    path('class/',views.Myrender.as_view()),
    path('con/',views.conview),
    path('context/',views.context_view.as_view()),
    path('myform/',views.myformview),
    path('c/',views.myformvieW.as_view()),
    #path('a/',views.check.as_view()),
    path('news/',views.news,{'template_name':'ahsannews.html'}),
    path('news2/',views.news,{'template_name':'ahsannews2.html'}),
    path('new/',views.newsbase.as_view()),
    path('helo/',views.newsbaseN.as_view()),
    path('helo1/',views.newsbaseN.as_view(template_name='ahsan.html'))
]
