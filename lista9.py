''' IMPORTACAO DE FUNCOES '''
from functools import reduce


'''
QUESTAO 1)
    A) Calcule o termo 'N' na seguencia de fibonacci
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


'''
    B) Calcule o MDC de dois numeros naturais
'''
def mdc(y, x):
    if y == x:
        return x
    elif y < x:
        aux = y
        y = x
        x = aux
        return mdc(y - x, x)
    else:
        return mdc(y - x, x)


'''
    E) Calcule o produto dos elementos de uma lista
'''
def produto(x, y):
    return x * y


def produto_lista(lista):
    return reduce(produto, lista)


'''
    F) Some os elementos pares e subtraia os impares
'''
def sumPAR_subIMP(lista):
    if lista == []:
        return 0
    elif (lista[0] % 2) == 0:
        return sumPAR_subIMP(lista[1:]) + lista[0]
    else:
        return sumPAR_subIMP(lista[1:]) - lista[0]


'''
    G) Dada uma lista ordenada insira um elemento
'''
def insere_ordenado(elem, lista):
    if lista == []:
        return [elem]
    elif lista[0] <= elem:
        return [lista[0]] + insere_ordenado(elem, lista[1:])
    else:
        return [elem] + lista


'''
    H) 
'''
def ordena_lista(lista, inte):
    if inte == len(lista):
        return lista
    else:
        return ordena_lista(insere_ordenado(lista[0], lista[1:]), inte + 1)