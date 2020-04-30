from django.shortcuts import render
from .models import Produto
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def list_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    try:
        data['list'] = Produto.objects.all()
    except:
         data['error'].append("Erro ao carregar Produto! ")
    return render(request, 'home.html', data)


@csrf_exempt
def new_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        try:
            if (id == -1):
                produto = Produto(descricao=descricao, preco=preco, estoque=estoque)
                produto.save()
            else:
                produto = Produto.objects.get(id=id)
                produto.descricao = descricao
                produto.preco = preco
                produto.estoque = estoque
                produto.save()
        except:
            data['error'].append("Erro ao cadastrar Produtos! ")
            return render(request, 'home.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar clientes! ")
            return render(request, 'home.html', data)
        return render(request, 'home.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'home.html', data)




def delete_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            produto = Produto.objects.get(id=id)
            produto.delete()
        except:
            data['error'].append("Erro ao deletar produto! ")
            return render(request, 'home.html', data)
        try:
            data['list'] = ProdutoS.objects.all()
        except:
            data['error'].append("Erro ao carregar clientes! ")
            return render(request, 'home.html', data)
        return render(request, 'home.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'home.html', data)
    

def update_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['produto'] = []
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            data['produto'].append(Produto.objects.get(id=id))
        except:
            data['error'].append("Erro ao carregar cliestes! ")
            return render(request, 'home.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar clientes! ")
            return render(request, 'home.html', data)
        return render(request, 'home.html', data)
    else:
        data['Error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'home.html', data)