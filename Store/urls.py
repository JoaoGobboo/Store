from django.urls import path
from . import views

urlpatterns = [
    path('', views.loja, name="Store"),
    path('produto/<int:produto_id>/', views.produto_detalhe, name="produto_detalhe"),
    path('carrinho/', views.carrinho, name="carrinho"),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name="adicionar_carrinho"),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name="remover_carrinho"),

    # CRUD de produtos unificado
    path('produtos/', views.produtos_crud, name='produtos_crud'),
]
