from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from main_app.models import Product
from django.http import JsonResponse




def cart_summary(request):
    return render(request, 'cart_summary.html')

def cart_add(request):
    p

def cart_delete(request):
    pass

def cart_update(request):
    pass

