from django.shortcuts import render
from core.models import CanalPovo
# Create your views here.
from django.views.generic import ListView

def qualquer():
    dados = CanalPovo.objects.all()
    # for d in dados:
    #     print(d.valor1) 
    for i in range(100000):
        print(i)

class CanalList(ListView):
    model = CanalPovo
    queryset = CanalPovo.objects.all()
    
    
    
    






