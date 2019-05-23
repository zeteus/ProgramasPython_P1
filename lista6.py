## EXERCICIOS DA LISTA SEIS ##

## Importacao de biblioteca
from functools import reduce


## QUESTAO 1) Dada uma lista, determine o seu maior elemento

# define o maior elemento dado dois numeros
def maior(a, b):
    if a < b:
        return b
    else:
        return a


# define o maior elemento de uma lista
def maiorLista(lista):
    return reduce(maior, lista)



## QUESTAO 2) Dada uma lista, verifique se ela nao eh decrescente

def decresce(a, b):
    if a > b:
        return True
    else:
        return False


# define se a lista eh decrescente
def listaNaoDecresce(lista):
    return [x < y for x in lista for y in lista[1:]]
    
    #return [x for x in range(0,len(lista)) if decresce(lista[x], lista[x+1])]

# QUESTAO 4)  Dada uma lista xs, fornecer uma tupla contendo o menor e o maior elemento dessa lista

# define o menor elemento dado dois numeros
def menor(a, b):
    if a > b:
        return b
    else:
        return a


# define o menor elemento de uma lista com paradigma aplicativo
def menorLista(lista):
    return reduce(menor, lista)

# funcao principal
def maior_e_menor(lista):
    tupla = (menorLista(lista), maiorLista(lista))
    return tupla