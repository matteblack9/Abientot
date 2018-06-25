from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^index/$', views.index, name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^product_detail/$', views.product_detail, name='product_detail'),
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
]
