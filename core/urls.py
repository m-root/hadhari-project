from django.conf.urls import url,include

from core import views

app_name = 'core'


daycare_urls = [
                url(r'^$', views.daycare_list, name='daycare_list'),

                url(r'^create$', views.create_daycare, name='daycare_create'),
                url(r'^(?P<pk>\d+)/', include([
                    url(r'^$',views.daycare_view, name='daycare_view'),
                    url(r'^owner$',views.daycare_owner_edit, name='owner'),
                    url(r'^images$',views.daycare_images, name='images'),
                    url(r'^images/add$',views.daycare_images, name='add_images'),
                    url(r'^edit$',views.daycare_edit, name='edit'),
                    url(r'^delete$',views.daycare_delete, name='delete'),
                    url(r'^contacts$',views.daycare_contacts, name='contacts'),
                    url(r'^contacts/',include([
                        url(r'^create$', views.daycare_contact_create, name='create'),
                        url(r'^(?P<contact_pk>\d+)/', include([
                            # url(r'^$', views.daycare_view, name='view')
                        ]))
                    ]))
                ]))
            ]


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^details$', views.details, name='details'),
    # url(r'^index/$', views.index2, name='index2'),
    #url(r'^daycare/create/$', views.create_daycare, name='daycare_create'),
    #url(r'^daycare/view/(?P<pk>\d+)/', views.daycare_view, name='daycare_view'),
    url(r'^daycares/', include(daycare_urls)),
    url(r'^listing$', views.listing, name='daycare_listing'),
    url(r'^organisations/', include([
        url(r'^$', views.organisation_list),
        url(r'^create$', views.organisation_create),

        url(r'^(?P<sub_domain>[\w-]+)/', include([

            url(r'^daycares/', include(daycare_urls)),

            #url(r'^$',views.daycare_view, name='view'),
            #url(r'^daycares',views.daycare_list, name='view'),
            #url(r'^images$',views.daycare_images, name='view'),
            # url(r'^images/add$',views.daycare_images, name='view'),
            # url(r'^edit$',views.daycare_edit, name='view'),
            # url(r'^delete$',views.daycare_delete, name='view'),
            # url(r'^contacts$',views.daycare_contacts, name='contacts'),
            # url(r'^contacts/',include([
            #     url(r'^create$', views.daycare_contact_create, name='view'),
            #     url(r'^(?P<contact_pk>\d+)/', include([
            #         # url(r'^$', views.daycare_view, name='view')
            #     ]))
            # ]))
        ]))
    ])),

    url(r'^admins/', include([
        url(r'^create$', views.admin_create),
    ])),

]
