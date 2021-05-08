from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view


"""
Metodo encargado de responder el valor con mas de 1000 divisores
GET : http://0.0.0.0:8000/api/v1/fibonacci/
"""
@api_view(['GET'])
def fibonacci(request):
    f1, f2 = 1,1    # Valores iniciales para Fn = Fn1 + Fn2
    dividers=3      # Variable encargada de contar cantidad de divisores (inicia en 3 porque ya exite Fn1 y Fn2)
    while dividers <= 1000:
        f1, f2 = f2, f1+f2
        dividers=dividers+1
    num_found=(f2-f1)
    print(f"El primer número de Fibonacci que tiene más de 1000 divisores es : {num_found}.")
    return  Response({'ok':True, 'result':num_found})