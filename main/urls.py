from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^index/product_details/(?P<productcode>.+)/$', views.product_details, name='product_details'),
    url(r'^product_details/(?P<productcode>.+)/$', views.product_details, name='product_details'),
	url(r'^(?P<pk>.+)/remove', views.remove_item_from_cart, name='remove_item_from_cart'),
	url(r'^(?P<pk>.+)/edit_quantity/(?P<edit_quantity>.+)/$', views.edit_quantity_of_cart, name='edit_quantity_of_cart'),
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
]
