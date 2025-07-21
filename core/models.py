from django.db import models
from django.contrib.auth.models import User

class Operacao(models.Model):
    OPERACOES = [
        ('+', 'Soma'),
        ('-', 'Subtração'),
        ('*', 'Multiplicação'),
        ('/', 'Divisão'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    operador = models.CharField(max_length=1, choices=OPERACOES)
    valor1 = models.FloatField()
    valor2 = models.FloatField()
    resultado = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)  # ✅ grava data e hora automaticamente

    def __str__(self):
        return f'{self.valor1} {self.operador} {self.valor2} = {self.resultado}'
