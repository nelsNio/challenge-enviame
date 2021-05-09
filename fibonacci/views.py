from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view



@api_view(['GET'])
def fibonacci(request):
    """
    Ejercicio 5: Análisis + Desarrollo
    Metodo encargado de responder el valor con mas de 1000 divisores
    GET : http://0.0.0.0:8000/api/v1/fibonacci/
    """
    f1, f2 = 1,1    # Valores iniciales para Fn = Fn1 + Fn2
    dividers=3      # Variable encargada de contar cantidad de divisores (inicia en 3 porque ya exite Fn1 y Fn2)
    while dividers <= 1000:
        f1, f2 = f2, f1+f2
        dividers=dividers+1
    num_found=(f2-f1)
    print(f"El primer número de Fibonacci que tiene más de 1000 divisores es : {num_found}.")
    return  Response({'ok':True, 'result':num_found})



def split_texts(text, size):
    """
    Divide el texto en puqueños grupos
    :param text:
    :param size:
    :return:
    """
    return [text[i:i + size] for i in range(0, len(text), size)]

def is_equal(texto: str):
    """
    Valida que la palabra o cadena de texto sea igual
    :param texto:
    :return: False or True
    """
    igual, aux = 0, 0
    for ind in reversed(range(0, len(texto))):
        if texto[ind].lower() == texto[aux].lower():
            igual += 1
        aux += 1
    return True if len(texto) == igual and len(texto) >= 2 else False


@api_view(['GET'])
def find_words(request):
    """
    Ejercicio 3: Análisis + Desarrollo
    Retorna una lista de textos encontrados cuya condicion
    es que es(son) igual al revés.
    """
    text = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood '
    result = []
    for x in range(3, len(text)):
        texts = split_texts(text, x)

        for strs in texts:
            if is_equal(strs):
                result.append(strs)
    return  Response({'ok':True, 'result':result})
