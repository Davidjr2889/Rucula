from django.db import models
from app.services.clientes.utils.choises import status, como_chegou, genero
# Create your models here.
class Customer(models.Model):
    
    cliente = models.CharField(blank=True, null=False)
    tutor = models.CharField(blank=True, null=False)
    status = models.CharField(blank=True, null=False, choices=status)
    cpf = models.CharField(blank=True, null=False)
    created_at = models.DateField(auto_now_add=True)
    como_chegou = models.CharField(blank=True, null=False, choices=como_chegou)
    endereco = models.CharField(blank=True, null=False)
    email = models.CharField(blank=True, null=False)
    bairro = models.CharField(blank=True, null=False)
    cidade = models.CharField(blank=True, null=False)
    estado = models.CharField(blank=True, null=False)
    cep = models.CharField(blank=True, null=False)
    ddd = models.CharField(blank=True, null=False)
    telefone = models.CharField(blank=True, null=False)
    raca = models.CharField(blank=True, null=False)
    genero = models.CharField(blank=True, null=False, choices=genero)
    peso = models.CharField(blank=True, null=False)
    receita = models.CharField(blank=True, null=False)
    aniversario = models.CharField(blank=True, null=False)
    gramas_por_dia = models.CharField(blank=True, null=False)
    assinatura = models.CharField(blank=True, null=False)
    gramas_por_dia = models.CharField(blank=True, null=False)
    kg_mes = models.CharField(blank=True, null=False)
    valor_kg = models.CharField(blank=True, null=False)
    valor_assiinatura_c_frete = models.CharField(blank=True, null=False)
    valor_assinatura_s_frete = models.CharField(blank=True, null=False)
    valor_frete = models.CharField(blank=True, null=False)

    class Meta:
        unique_together = (
            (
                'cliente',
                'tutor'
            )
        )
        db_table = 'table_clientes'