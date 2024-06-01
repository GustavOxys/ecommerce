from django.urls import path
from .views import Create, Upload, Login, Logout


app_name = 'profile'


urlpatterns = [
    path('', Create.as_view(), name='create'),
    path('upload/', Upload.as_view(), name='upload'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]