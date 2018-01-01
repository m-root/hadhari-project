from . import views
from django.conf.urls import url, include

urlpatterns = (
    url(r'^$', views.index, name='index'),

    url(r'^new_member$', views.new_member, name='new_member'),
    url(r'^members$', views.list_member, name='members'),
    url(r'^edit_member$', views.edit_member, name='edit_member'),#TODO: to be returned with pk
    url(r'^member_details$', views.member_details, name='member_details'),#TODO: to be returned with pk
    url(r'^new_user$', views.new_user, name='new_user'),
    url(r'^users$', views.list_user, name='users'),
    url(r'^edit_user$', views.edit_user, name='edit_user'),  # TODO: to be returned with pk
    url(r'^user_details$', views.user_details, name='user_details'),  # TODO: to be returned with pk

    # url(r'events/', include([
    #     url(r'create/', views.events_create, name='create')
    # ]), name='events'),

)
