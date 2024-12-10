from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from main_app.models import Product
from django.http import JsonResponse




def cart_summary(request):
    return render(request, 'cart_summary.html')

def cart_add(request):
    #get cart from session
    cart = Cart(request)
    #if request is post 
    if request.POST.get('action') == 'post':
        #get product_id from the request
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'product': product.name})
        return response
        

   
       


def cart_delete(request):
    pass

def cart_update(request):
    pass

