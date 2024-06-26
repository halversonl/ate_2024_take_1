"""
URL configuration for ate_2024_take_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from hello.views import index
from pages.views import homepage_view, about_view
from activity_input.views import activity_example_view, activity_input_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', index),
    path('', homepage_view, name='home'),
    path('about/', about_view),
    path('example/', activity_example_view),
    path('upload/', activity_input_view)
]
