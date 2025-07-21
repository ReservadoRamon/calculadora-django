from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao
from django.views.decorators.csrf import csrf_exempt
import re

@login_required
def calculadora(request):
    operacao = request.session.get("operacao_atual", "")
    resultado = request.session.get("resultado", "")
    limpar_visao = request.session.get("limpar_visao", False)
    

    if request.method == "POST":
        btn = request.POST.get("btn")

        if btn == "C":
            operacao = ""
            resultado = ""
            request.session["limpar_visao"] = False
        

        elif btn == "=":
            try:
                operacao_formatada = tratar_porcentagem(operacao)
                resultado = str(eval(operacao_formatada))
                valor1, operador, valor2 = separar_operacao(operacao)
                if operador:
                    Operacao.objects.create(
                        usuario=request.user,
                        valor1=valor1,
                        valor2=valor2,
                        operador=operador,
                        resultado=resultado
                    )
                    
                request.session["limpar_visao"] = True
            except Exception:
                resultado = "Erro"
                request.session["limpar_visao"] = True

        elif btn == "+/-":
            operacao = inverter_sinal(operacao)

        else:
            if limpar_visao:
                operacao = ""
                resultado = ""
                request.session["limpar_visao"] = False

            operacao += btn

        request.session["operacao_atual"] = operacao
        request.session["resultado"] = resultado

    historico = Operacao.objects.filter(usuario=request.user).order_by('-criado_em')


    return render(request, "core/calculadora.html", {
        "operacao_atual": operacao,
        "resultado": resultado,
        "historico": historico
    })

def tratar_porcentagem(expr):
    # Substitui "n%" por "(n/100)"
    return re.sub(r'(\d+)%', r'(\1/100)', expr)

def inverter_sinal(expr):
    # Inverte o sinal do último número digitado
    match = re.search(r'(-?\d+\.?\d*)$', expr)
    if match:
        numero = match.group(1)
        if numero.startswith('-'):
            invertido = numero[1:]
        else:
            invertido = f"-{numero}"
        return expr[:match.start()] + invertido
    return expr

def separar_operacao(expressao):
    match = re.match(r'(\d+(?:\.\d+)?)([\+\-\*/])(\d+(?:\.\d+)?)(%?)$', expressao)
    if match:
        valor1 = float(match[1])
        operador = match[2]
        valor2 = float(match[3])
        if match[4] == '%':
            valor2 /= 100
        return valor1, operador, valor2
    return None, None, None

@csrf_exempt
@login_required
def limpar_historico(request):
    if request.method == "POST":
        Operacao.objects.filter(usuario=request.user).delete()
        request.session["operacao_atual"] = ""
        request.session["resultado"] = ""
        request.session["limpar_visao"] = False
    return redirect('calculadora')
