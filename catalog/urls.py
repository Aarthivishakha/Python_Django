from django.conf.urls import url

from catalog import views

urlpatterns = [
    url(r'^products/$', views.product_list, name='product-list'),
    url(r'^products/export/$', views.product_export, name='product-export'),
    url(r'^quote/$', views.quote, name='quote'),
]
