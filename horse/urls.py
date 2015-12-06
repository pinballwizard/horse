from django.conf.urls import include, url
from django.contrib import admin
from flatlease import views as flat_views
from car_leasing import views as car_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

flatlease_url = [
    url(r'^$', flat_views.calculator, name='calculator'),
    url(r'^addition$', flat_views.update, name='update'),
    url(r'^update_id=(?P<client_id>\d+)$', flat_views.update, name='update'),
    url(r'^client_id=(?P<client_id>\d+)$', flat_views.client_page, name='client_page'),
    url(r'^search$', flat_views.search, name='search'),
    url(r'^statistics$', flat_views.statistics, name='statistics'),
]

# car_leasing_url = [
#     url(r'^$', name=''),
# ]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^login$', flat_views.user_login, name='login'),
    url(r'^logout$', flat_views.user_logout, name='logout'),
    url(r'^$', flat_views.calculator, name='calculator'),
    url(r'^flat/', include(flatlease_url)),
    # url(r'^car/', include(car_leasing_url)),
    url(r'^test', flat_views.test_page, name='test_page'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='flatlease/robots.txt'), name='robots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
