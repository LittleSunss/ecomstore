from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.show_cart, name='cart')
)
