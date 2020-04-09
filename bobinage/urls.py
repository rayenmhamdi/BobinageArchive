# in urls.py of the application

from django.urls import path

from . import views

app_name = 'bobinage'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
]
