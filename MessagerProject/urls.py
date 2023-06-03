from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_CSRF, name='index'),
    path('list', views.list_dialog, name='list'),
    path('create', views.create, name='create'),
    path('connect', views.connect, name='create'),
    path('message', views.messages, name='create'),
]