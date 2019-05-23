# import da reduce
from functools import reduce


# Identifique o menor elemento de uma lista

# define o menor elemento dado dois numeros
def menor(a, b):
    if a > b:
        return b
    else:
        return a


# define o menor elemento de uma lista com paradigma aplicativo
def menorListaAplic(lista):
    return reduce(menor, lista)


# define o menor elemento de uma lista com paradigma recursivo
def menorListaRec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return menor(menorListaRec(lista[1:]),lista[0])


# calcule o somatorio de uma lista
def somatorioRec(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + somatorioRec(lista[1:])


# Ordenar uma lista

# funcao de trocar valores
