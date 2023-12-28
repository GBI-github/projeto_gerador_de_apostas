from django.shortcuts import render
from .forms import Aposta
from .models import Apostas_1
import random

def gerar_comb_aleatoria(quantidade):
    combinacoes = []
    for _ in range(quantidade):
        numeros = random.sample(range(1,61),6)
        num_str = ",".join(map(str,numeros))
        combinacoes.append(num_str)

    return combinacoes


def fazer_apostas(request):
    form = Aposta(request.POST or None)
    
    if form.is_valid():
        quant_aposta = form.cleaned_data["quant"]
        combinacões = gerar_comb_aleatoria(quant_aposta)

        for comb in combinacões:
            Apostas_1.objects.create(numeros=comb)

    return render(request,"apostas/apostas.html",{'form':form, "num_comb":combinacões})