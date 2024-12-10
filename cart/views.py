from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from main_app.models import Product
from django.http import JsonResponse




def cart_summary(request):
     cart = Cart(request)
     cart_products = cart.get_prods()
     return render(request, 'cart_summary.html', {'cart_products': cart_products})
    

def cart_add(request):
    #get cart from session
    cart = Cart(request)
    #if request is post 
    if request.POST.get('action') == 'post':
        #get product_id from the request
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response
        

   
       


def cart_delete(request):
    pass

def cart_update(request):
    pass

