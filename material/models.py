from django.db import models
from django.utils import timezone

class Material(models.Model):
    nome = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200,blank=True)
    descrição = models.TextField()
    lote = models.CharField(max_length=10)
    data_registro = models.DateTimeField(default=timezone.now)
    preco_de_compra = models.DecimalField(max_digits=6,decimal_places=2)
    preco = models.DecimalField(max_digits=6,decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
    

