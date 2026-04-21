from django.urls import path
from .views import listar_tarefas, buscar_por_id

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/<int:id>', buscar_por_id),
]