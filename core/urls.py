from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home', views.home, name='home'),
    path('company', views.company, name='company'),
    path('team', views.team, name='team'),
    path('features', views.features, name='features')
]