#==========================#
# EXERCICIOS DA LISTA SETE #
#==========================#

# IMPORTACAO DE FUNCOES
from functools import reduce


# QUESTAO 1)
#   Dada uma lista de numeros

# A) Retorna o maior elemento da lista

# funcao de que retorna o maior de dois elementos
def maior(a, b):
    if a > b:
        return a
    else:
        return b


# funcao principal
def maiorLista(lista):
    return reduce(maior, lista)


# B) Retorna a soma dos elementos da lista

# funcao que retorna a soma de dois elementos
def soma(a, b):
    return a + b


# funcao que faz o somatorio da lista; (tambem usada no exercicio D)
def somatorio(lista):
    return reduce(soma, lista)


# C) Retornar quantas vezes o primeiro elemento ocorre na lista

# retorna o primeiro elemento da lista
def primeiroLista(lista):
    return lista[0]


# funcao principal que calcula as ocorrencias
def ocorrencias(lista):
    primeiro = primeiroLista(lista)
    listaOcorre = [x for x in lista if x == primeiro]
    return len(listaOcorre)


# D) Retornar a media aritimetica da lista

# calcula o numero de elementos da lista
def nElementos(lista):
    return len(lista)


# Retorna a media dos elementos
def mediaLista(lista):
    return somatorio(lista) / nElementos(lista)


# E) Retorna o elemento mais proximo da media dos elementos

# funcao de que retorna o menor de dois elementos
def menor(a, b):
    if a < b:
        return a
    else:
        return b


# retorna o menor elemento da lista
def menorLista(lista):
    return reduce(menor, lista)


# calcula a diferenca de cada elemento
def diferenca(a, b):
    return a - b


# funcao principal
def numeroMedia(lista):
    listaDiferenca = [diferenca(x, mediaLista(lista)) for x in lista]
    listaDiferencaPos = list(map(abs, listaDiferenca))
    indice = listaDiferencaPos.index(menorLista(listaDiferencaPos))
    return lista[indice]


# F) Retorna a soma dos elementos negativos da lista

# funcao principal
def somaNegativos(lista):
    listaNegativos = [x for x in lista if x < 0]
    return somatorio(listaNegativos)


# QUESTAO 2)
#   Dada uma lista de strings

# A) Retornar a string com mais caracteres

# retorna a maior string, dada duas
def maiorString(a, b):
    if len(a) > len(b):
        return a
    else:
        return b


# funcao principal
def maiorStringLista(lista):
    return reduce(maiorString, lista)


# B) Retornar a media de vogais nas strings

# funcao que retorna a soma de dois elementos
def somaLetras(a, b):
    return len(a) + len(b)


# funcao que faz o somatorio do numero de letras numa lista;
def somatorioLetras(lista):
    return reduce(somaLetras, lista)


# Retorna a media de letras da lista
def mediaLetrasLista(lista):
    return somatorioLetras(lista) / nElementos(lista)