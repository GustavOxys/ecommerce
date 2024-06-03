from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListProduct(ListView):
    model = models.Product
    template_name = 'list.html'
    context_object_name = 'products'
    paginate_by = 9
    

class DetailProduct(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detail Product')


class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Add to cart')


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove from cart')


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Cart')


class Checkout(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Checkout')




