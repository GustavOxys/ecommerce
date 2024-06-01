from django.urls import path
from .views import Pay, CompleteOrder, Detail


app_name = 'order'

urlpatterns = [
    path('', Pay.as_view(), name='pay'),
    path('completeorder/', CompleteOrder.as_view(), name='completeorder'),
    path('detail/', Detail.as_view(), name='detail'),
]