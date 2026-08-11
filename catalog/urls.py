from django.conf.urls import patterns, url

urlpatterns = patterns('catalog.views',
    url(r'^products/$', 'product_list', name='product-list'),
    url(r'^products/export/$', 'product_export', name='product-export'),
    url(r'^quote/$', 'quote', name='quote'),
)
