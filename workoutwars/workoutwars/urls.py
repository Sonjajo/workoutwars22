"""workoutwars URL Configuration

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
    1. url() deprecated in Django 4.0+, use re_path instead. https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to
"""
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('workoutwarsapp.urls')),
]
