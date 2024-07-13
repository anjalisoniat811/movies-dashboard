from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for serving index.html
    path('api/', views.proxy_api_request, name='proxy_api'),  # Route for proxying API requests
]