from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('company', views.company, name='company'),
    path('team', views.team, name='team'),
    path('features', views.features, name='features'),
    path('blog', views.blog, name='blog')
]