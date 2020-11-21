"""onlinequiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.Login_Page.as_view(),name='login'),
    path('',views.Quiz_Welcome_Page.as_view(),name='index'),
    path('question1/',views.Quiz_Page1.as_view(),name='question1'),
    path('question2/',views.Quiz_Page2.as_view(),name='question2'),
    path('question3/',views.Quiz_Page3.as_view(),name='question3'),
    path('question4/',views.Quiz_Page4.as_view(),name='question4'),
    path('question5/',views.Quiz_Page5.as_view(),name='question5'),
    path('question6/',views.Quiz_Page6.as_view(),name='question6'),
    path('question7/',views.Quiz_Page7.as_view(),name='question7'),
    path('question8/',views.Quiz_Page8.as_view(),name='question8'),
    path('question9/',views.Quiz_Page9.as_view(),name='question9'),
    path('question10/',views.Quiz_Page10.as_view(),name='question10'),
    path('result/',views.Quiz_Result.as_view(),name='result'),
]