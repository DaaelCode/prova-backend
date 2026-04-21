from django.http import JsonResponse
from .models import Tarefa


def listar_tarefas(request):
    tarefas = Tarefa.objects.values(
        'id',
        'titulo',
        'descricao',
        'status',
        'data_criacao',
        'data_entrega',
        'usuario_responsavel__nome'
    )
    return JsonResponse(list(tarefas), safe=False)

def buscar_por_id(request, id):
    try:
        tarefas = Tarefa.objects.get(id=id)
        return JsonResponse({
            'id': tarefas.id,
            'titulo': tarefas.titulo,
            'descricao': tarefas.descricao,
            'status': tarefas.status,
            'data_criacao': tarefas.data_criacao,
            'data_entrega': tarefas.data_entrega,
            
        })
    
    except Tarefa.DoesNotExist:
           return JsonResponse({'ERRO': '404 Not Found'}) 