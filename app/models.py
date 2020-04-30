from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao = models.CharField(max_length=50, blank=False)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    estoque = models.IntegerField(blank=True)
 
    def __str__(self):
        return self.descricao