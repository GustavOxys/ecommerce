from django.urls import path
from .views import ListProduct, DetailProduct, AddToCart, RemoveFromCart, Cart, Checkout


app_name = 'product'

urlpatterns = [
    path('', ListProduct.as_view(), name='list'),
    path('<slug>', DetailProduct.as_view(), name='detail'),
    path('addtocart/', AddToCart.as_view(), name='addtocart'),
    path('removefromcart/', RemoveFromCart.as_view(), name='removefromcart'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout')
]