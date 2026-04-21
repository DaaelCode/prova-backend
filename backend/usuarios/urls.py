from django.urls import path
from .views import listar_usuarios, buscar_por_id

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuarios/<int:id>', buscar_por_id),    
]