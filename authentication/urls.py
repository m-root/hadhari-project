from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import account_activation_sent
from authentication import views as core

app_name = 'authentication'

urlpatterns = [

    url(r'^login/$', core.LoginView.as_view(), name='login'),
    url(r'^signup/$', core.RegisterView.as_view(), name='signup'),
    url(r'^logout/$', core.LogoutView.as_view(), name='logout'),

    url(r'^password_reset/$',
        auth_views.password_reset,
        {
            'template_name': 'authentication/registration/password_reset_form.html',
            'from_email':'no-reply@mail.tt.com'
        },
        name='password_reset'
        ),
    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'authentication/registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core.activate, name='activate'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {
            'post_reset_redirect':'authentication:password_reset_complete',
            'template_name': 'authentication/registration/password_reset_confirm.html'
        },
        name='password_reset_confirm'
        ),
    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        {
            'template_name': 'authentication/registration/password_reset_complete.html'
        },
        name='password_reset_complete'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),

]
