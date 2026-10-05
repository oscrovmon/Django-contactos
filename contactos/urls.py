from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/<int:pk>/', views.ficha, name='ficha'),
    path('contacto/nuevo/', views.nuevo, name='nuevo'),
    path('contacto/<int:pk>/editar/', views.editar, name='editar'),
    path('contacto/<int:pk>/eliminar/', views.eliminar, name='eliminar'),
]