from django.urls import path
from . import views

urlpatterns = [
path('productos/', views.DB_Productos, name='lista de productos'),
]
