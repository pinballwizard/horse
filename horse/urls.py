from django.conf.urls import include, url
from django.contrib import admin
from base import views as base_views
from flatlease import views as flat_views
from car_leasing import views as car_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

base_url = [
    url(r'^search$', flat_views.search, name='search'),
    url(r'^addition$', flat_views.update, name='update'),
    url(r'^update_id=(?P<client_id>\d+)$', flat_views.update, name='update'),
    url(r'^client_id=(?P<client_id>\d+)$', flat_views.client_page, name='client_page'),
]

flatlease_url = [
    url(r'^calculator$', flat_views.calculator, name='calculator'),
    url(r'^statistics$', flat_views.statistics, name='statistics'),
]

car_leasing_url = [
    url(r'^search$', car_views.car_search, name='search'),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', base_views.user_login, name='login'),
    url(r'^logout$', base_views.user_logout, name='logout'),
    url(r'^$', base_views.choice, name='choice'),
    url(r'^calculator$', flat_views.calculator, name='calculator'),
    url(r'^', include(base_url, namespace='base', app_name='base')),
    url(r'^flat/', include(flatlease_url, namespace='flat', app_name='flat')),
    url(r'^car/', include(car_leasing_url, namespace='car', app_name='car')),
    url(r'^test', base_views.test_page, name='test_page'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='flatlease/robots.txt'), name='robots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
