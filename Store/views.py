from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Carrinho, CarrinhoItem, Categoria
from .forms import ProdutoForm

# =========================
# Carrinho
# =========================
def get_carrinho(request):
    carrinho_id = request.session.get("carrinho_id")
    if not carrinho_id:
        carrinho = Carrinho.objects.create()
        request.session["carrinho_id"] = carrinho.id
    else:
        carrinho = Carrinho.objects.get(id=carrinho_id)
    return carrinho

def loja(request):
    lista_produtos = Produto.objects.all()
    context = {
        'titulo': 'Minha Loja Bonita',
        'usuario': 'Jorge',
        'lista': lista_produtos,
    }
    return render(request, 'loja.html', context)

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto_detalhe.html', {"produto": produto})

def adicionar_ao_carrinho(request, produto_id):
    carrinho = get_carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    item, created = CarrinhoItem.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not created:
        item.quantidade += 1
        item.save()
    return redirect("carrinho")

def remover_do_carrinho(request, item_id):
    carrinho = get_carrinho(request)
    item = get_object_or_404(CarrinhoItem, id=item_id, carrinho=carrinho)
    item.delete()
    return redirect("carrinho")

def carrinho(request):
    carrinho = get_carrinho(request)
    return render(request, "carrinho.html", {"carrinho": carrinho})

# =========================
# CRUD de Produtos
# =========================

def produtos_crud(request):
    lista_produtos = Produto.objects.all()
    form_criar = ProdutoForm()

    if request.method == "POST":
        acao = request.POST.get("acao")
        produto_id = request.POST.get("produto_id")

        if acao == "deletar" and produto_id:
            produto = get_object_or_404(Produto, id=produto_id)
            produto.delete()
            return redirect("produtos_crud")

        elif acao == "editar" and produto_id:
            produto = get_object_or_404(Produto, id=produto_id)
            form_editar = ProdutoForm(request.POST, instance=produto)
            if form_editar.is_valid():
                form_editar.save()
                return redirect("produtos_crud")

        elif acao == "criar":
            form_criar = ProdutoForm(request.POST)
            if form_criar.is_valid():
                form_criar.save()
                return redirect("produtos_crud")

    context = {
        "lista": lista_produtos,
        "form_criar": form_criar,
    }
    return render(request, "produtos_crud.html", context)
