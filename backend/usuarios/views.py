from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_por_id(request, id):
    try:
        usuarios = Usuario.objects.get(id=id)
        return JsonResponse({
            'id': usuarios.id,
            'nome': usuarios.nome,
            'email': usuarios.email,
            'ativo': usuarios.ativo,
            'data_criacao': usuarios.data_criacao,
        })
    
    except Usuario.DoesNotExist:
           return JsonResponse({'ERRO': '404 Not Found'}) 