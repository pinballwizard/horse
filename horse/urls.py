"""horse URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from flatlease import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', views.calculator, name='calculator'),
    url(r'^addition$', views.addition, name='addition'),
    # url(r'^addition(?P<client_id>[0-9]+)$', views.addition, name='addition'),
    url(r'^update_id=(?P<client_id>[0-9]+)$', views.addition, name='update_id'),
    url(r'^update_id=(?P<client_id>[0-9]+)$', views.client_update, name='client_update'),
    url(r'^client_id=(?P<client_id>[0-9]+)$', views.client_page, name='client_page'),
    url(r'^test', views.test_page, name='test_page'),
    url(r'^search$', views.search, name='search'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^statistics$', views.statistics, name='statistics'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='flatlease/robots.txt'), name='robots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)