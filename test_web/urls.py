"""
URL configuration for test_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from posts.views import index, home, post_list, post_detail, post_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('home/', home),
    path("posts/", post_list, name="post_list"),
    path("posts/<int:post_id>", post_detail, name="post_detail"),
    path("posts/create", post_create, name="post_create")
]
