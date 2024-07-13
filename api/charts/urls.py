from django.urls import path
from . import views
from django.conf import settings
from django.views.generic.base import TemplateView
from django.urls import include, re_path

urlpatterns = [
    path('movie_data/', views.MoviesClass.as_view()),
    # re_path('movies/', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('', views.getData, name='get_year'),
    # path('post/', views.postData),
]