# from django.conf.urls.defaults import *
from django.conf.urls import patterns, url
from catalog import views
# urlpatterns = patterns('ecomstore.catalog.views',
#     (r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),
#     (r'^category/(?P<category_slug>[-\w]+)/$',
#         'show_category', {
#         'template_name':'catalog/category.html'},'catalog_category'),
#     (r'^product/(?P<product_slug>[-\w]+)/$',
#         'show_product', {
#         'template_name':'catalog/product.html'},'catalog_product'),
# )
urlpatterns = patterns('',
    # url(r'^$', 'index', {'template_name': 'catalog/index.html'},'calalog_home'),
    url(r'^$', views.index, name='index'),

    # url(r'^category/(?P<category_slug>[-\w]+)/$','show_category', {'template_name':'catalog/category.html'}, 'catalog_category'),
    # url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', {'template_name':'catalog/product.html'}, 'catalog_product'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category, name='categary'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product,name='product'),
)
