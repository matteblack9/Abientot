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
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
<<<<<<< HEAD
    url(r'^(?P<quer>.+)/$', views.search, name = 'index'),
=======
    url(r'^search', views.search,name='search')
>>>>>>> 4e10e279397387f232241728ee6263c89c9ad3a7
]
