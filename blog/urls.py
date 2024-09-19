from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloWorld.as_view(), name='home'),
    path('price/', views.GetBestPrice.as_view(), name='price'),
]