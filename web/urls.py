from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
