from django.shortcuts import render
from django.template import RequestContext

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from catalog.forms import ProductAddToCartForm
from . import cart
# Create your views here.
def show_cart(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart' 
    cart_subtotal = cart.cart_subtotal(request)
    # cart_item_count = cart.cart_item_count(request)
    # cart_item_count = cart.get_cart_items(request)
    # page_title = 'Shopping Cart'
    return render(request, 'cart.html', locals())

