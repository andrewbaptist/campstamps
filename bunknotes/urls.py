from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boo', views.families, name='index22'),
]
