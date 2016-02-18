"""hamath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from hamath import views

from views import HomeView, LogoutView#, LoginView, SignUpView, StudentView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='Home'),
    url(r'^home/$', HomeView.as_view(), name='Home'),
    #url(r'^student/$', StudentView.as_view(), name='Student'),
    url(r'^student/$', views.Student, name='Student'),
    #url(r'^signup/$', SignUpView.as_view(), name='SignUp'),
    url(r'^signup/$', views.SignUp, name='SignUp'),
    #url(r'^login/$', LoginView.as_view(), name='Login'),
    url(r'^login/$', views.Login, name='Login'),
    url(r'^logout/$', LogoutView.as_view(), name='Logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if (settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)