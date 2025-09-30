from django.shortcuts import render

def index(request):
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operacao = request.POST.get("operacao")

            if operacao == "soma":
                resultado = num1 + num2
            elif operacao == "subtracao":
                resultado = num1 - num2
            elif operacao == "multiplicacao":
                resultado = num1 * num2
            elif operacao == "divisao":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    erro = "Não é possível dividir por zero!"
        except Exception as e:
            erro = f"Erro: {str(e)}"

    return render(request, "calculadora/index.html", {"resultado": resultado, "erro": erro})
