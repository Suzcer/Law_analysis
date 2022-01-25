"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 针对不同的功能，指向不同的views
    path('index/', views.index),  # 最初一版
    path('preload/', views.preload),  # 提前加载页
    path('login/', views.login),  # 默认的登录界面
    path('home/', views.home),  # 主页
    path('search/', views.search),  # 搜索页
    path('upload/', views.upload),  # 上传页
    path('textinput/', views.textinput),  # 文字输入页
    path('demo/', views.demo),
    path('detail/', views.detail),
    path('readme/', views.readme),
    # path('todos/',views.todos),
]
