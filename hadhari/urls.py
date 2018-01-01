"""boxgirls URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from web import views as web

urlpatterns = [
    url(r'^', include('web.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^calender/', include('calender.urls')),
    url(r'^profiles/', include('core.urls', namespace='core')),
    url(r'^reports/', include('reports.urls', namespace='reports')),

    url(r'^login/$', web.LoginView.as_view(), name='login'),
    url(r'^logout/$', web.LogoutView.as_view(), name='logout'),

    url(r'^password_reset/$',
        auth_views.password_reset,
        {'template_name': 'web/registration/password_reset_form.html'},
        name='password_reset'
        ),
    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'web/registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'web/registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        {'template_name': 'web/registration/password_reset_complete.html'},
        name='password_reset_complete'),

    url(r'^admin/', admin.site.urls),

]

# serve static and media files in development
if settings.DEBUG:
    urlpatterns = urlpatterns \
                  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
