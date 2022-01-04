from django.urls import path
from .import views

urlpatterns = [
    path( 'begin/', views.begin, name = 'begin'),

    path( 'delete/<str:id>/' , views.delete, name = 'delete'),

    path( 'read/<str:id>/' , views.read , name = 'read'),

    path('create/', views.create, name= 'create'),
    
]
