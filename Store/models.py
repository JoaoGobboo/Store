from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.CharField(max_length=100, blank=True)  # texto opcional
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho {self.id}"

    def total(self):
        return sum(item.subtotal() for item in self.itens.all())

class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name="itens", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"
