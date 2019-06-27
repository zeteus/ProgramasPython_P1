#==========================#
# EXERCICIOS DA LISTA SETE #
#==========================#

# IMPORTACAO DE FUNCOES
from functools import *

# QUESTAO 1)
#   Dada uma lista de numeros

# A) Retorna o maior elemento da lista

## funcao de que retorna o maior de dois elementos
def maior(a, b):
    if a > b:
        return a
    else:
        return b


## funcao principal
def maiorLista(lista):
    return reduce(maior, lista)


# B) Retorna a soma dos elementos da lista

## funcao que retorna a soma de dois elementos
def soma(a, b):
    return a + b


## funcao que faz o somatorio da lista; (tambem usada no exercicio D)
def somatorio(lista):
    return reduce(soma, lista)


# C) Retornar quantas vezes o primeiro elemento ocorre na lista

## retorna o primeiro elemento da lista
def primeiroLista(lista):
    return lista[0]


## funcao principal que calcula as ocorrencias
def ocorrencias(lista):
    primeiro = primeiroLista(lista);
    listaOcorre = [x for x in lista if x == primeiro]
    return len(listaOcorre)

# D) Retornar a media aritimetica da lista

## calcula o numero de elementos da lista
def nElementos(lista):
    return len(lista)


## Retorna a media dos elementos
def mediaLista(lista):
    return somatorio(lista) / nElementos(lista)


# E) Retorna o elemento mais proximo da media dos elementos

## funcao de que retorna o menor de dois elementos
def menor(a, b):
    if a < b:
        return a
    else:
        return b


## retorna o menor elemento da lista
def menorLista(lista):
    return reduce(menor, lista)


## calcula a diferenca de cada elemento
def diferenca(a, b):
    return a - b


## funcao principal
def numeroMedia(lista):
    listaDiferenca = [diferenca(x, mediaLista(lista)) for x in lista]
    listaDiferencaPos = list(map(abs, listaDiferenca))
    indice = listaDiferencaPos.index(menorLista(listaDiferencaPos))
    return lista[indice]


# F) Retorna a soma dos elementos negativos da lista

## funcao principal
def somaNegativos(lista):
    listaNegativos = [x for x in lista if x < 0]
    return somatorio(listaNegativos)


# QUESTAO 2)
#   Dada uma lista de strings

# QUESTAO 3)
#   Uma funcao que traduza o codigo das duas amigas

## funcao que retorna o caracter correspondente ao numero de entrada
def comparaCod(num):
    if num == 0:
        return ' '
    elif num == 1:
        return 'a'
    elif num == 2:
        return 'b'
    elif num == 3:
        return 'c'
    elif num == 4:
        return 'd'
    elif num == 5:
        return 'e'
    elif num == 6:
        return 'f'
    elif num == 7:
        return 'g'
    elif num == 8:
        return 'h'
    elif num == 9:
        return 'i'
    elif num == 10:
        return 'j'
    elif num == 11:
        return 'k'
    elif num == 12:
        return 'l'
    elif num == 13:
        return 'm'
    elif num == 14:
        return 'n'
    elif num == 15:
        return 'o'
    elif num == 16:
        return 'p'
    elif num == 17:
        return 'q'
    elif num == 18:
        return 'r'
    elif num == 19:
        return 's'
    elif num == 20:
        return 't'
    elif num == 21:
        return 'u'
    elif num == 22:
        return 'v'
    elif num == 23:
        return 'w'
    elif num == 24:
        return 'x'
    elif num == 25:
        return 'y'
    elif num == 26:
        return 'z'


## funcao que traduz o a frase das amigas
def traduz(lista):
    listaTrad = [comparaCod(x) for x in lista]
    return ''.join(listaTrad)
    


# QUESTAO 4)listaD
#   Faca um programalistaD que receba uma lista com o numero de faltas e os times que jogaram e faca:

# A) O total de faltlistaDas do jogo
## soma o numero de faltas
def faltas(f):
    return f[0] + f[1]


## calcula as faltas de acordo com a lista dada
def totalFaltas(lista):
    return faltas(lista[2])


# B) O time que fez mais faltas
## calcula o qual eh o menor numero de faltas e retorna o indice do time que tem esse numero
def maisFaltas(f):
    if f[0] > f[1]:
        return 0
    else:
        return 1


## funcao principal que retorna o time mais faltoso
def timeMaisFaltas(lista):
    return lista[maisFaltas(lista[2])]


# C) O time que fez menos faltas
## calcula o qual eh o menor numero de faltas e retorna o indice do time que tem esse numero
def menosFaltas(f):
    if f[0] < f[1]:
        return 0
    else:
        return 1


## funcao principal que retorna o time menos faltoso
def timeMenosFaltas(lista):
    return lista[menosFaltas(lista[2])]


# QUESTAO 5)
## funcao que retorna o numero mais proximo da media

## QUESTAO IGUAL A LETRA "E" DA PRIMEIRA QUESTAO

# QUESTAO 6)

## Dada uma lista de alunos com suas idades e alturas e:

# A) Calcule a media da altura da turma
## funcao que cria uma lista somente com as alturas da turma
def alturas(l):
    listaAlt = [x[1] for x in l]
    return listaAlt


## funcao que soma as alturas da turma
def somaAlt(l):
    return reduce(soma, alturas(l))


## funcao principal que calcula a media de alturas da turma
def mediaAlt(lista):
    return somaAlt(lista) / len(lista)


# B) Calcula quantos alunos com mais de 13 anos que estao abaixo da media da turma
def contaBaixinhos(lista):
    ## funcao recursiva que soma em quant sempre que encontrar um baixinho
    def recursiva(l, q, m):
        if len(l) == 0:
            return q
        elif l[0][0] > 13 and l[0][1] < m:
            q = q + 1
            return recursiva(l[1:], q, m)
        else:
            return recursiva(l[1:], q, m)

    quant = 0
    return recursiva(lista, quant, mediaAlt(lista))


# QUESTAO 7)

# A) Crie uma lista com os signos
def criaSignos():
    listaSignos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
    return listaSignos

# B) Crie uma lista com a data de aniversario dos membros
def dataAniversario():
    listaDatas = [1973, 2004, 2000, 1969]
    return listaDatas

# C) Usando as lista de 'A' e 'B' mostre o signo de cada membro da familia
def mostraSigno():
    listaSig = criaSignos()
    listaDat = dataAniversario()
    listaComparacao = [listaSig[x % 12] for x in listaDat]
    return listaComparacao


# QUESTAO 8)

## verificar se uma lista qualquer esta ordenada
def esta_ordenado(lista):
    if type(lista[0]) == list:
        return esta_ordenado(lista[0])
    elif len(lista) == 2:
        if type(lista[1]) == list:
            return esta_ordenado(lista[1])
        elif lista[0] < lista[1]:
            return True
        else:
            return False
    elif type(lista[1]) == list:
        if lista[0] > lista[2]:
            return False
        else:
            return esta_ordenado(lista[1:])
    elif lista[0] > lista[1] and type(lista[1]) != list:
        return False
    else:
        return esta_ordenado(lista[1:])


# QUESTAO 9)

## retorna a posicao da primeira ocorrencia de um numero dado
def primeira_ocorrencia(lista, num):
    def somaPosicao(l, n):
        if n == l[0]:
            return 0
        else:
            return 1 + somaPosicao(l[1:], n)
    if lista == []:
        return -2
    elif num in lista:
        return somaPosicao(lista, num)
    else:
        return -1


# QUESTAO 10)

## Funcao auxiliar para as questoes
def retira_repetidos(lista):
        if len(lista) == 0:
            return []
        elif lista[0] in lista[1:]:
            return retira_repetidos(lista[1:])
        else:
            return [lista[0]] + retira_repetidos(lista[1:])


# A) receba duas lista e faca a uniao entre elas
def uniao(lista1, lista2):
    return retira_repetidos(lista1 + lista2)


# B) receba duas lista e faca a intercecao entre elas
def intercecao(lista1, lista2):
    def gera_intercecao(lista1, lista2):
        if lista1 == []:
            return []
        elif lista1[0] in lista2:
            return [lista1[0]] + intercecao(lista1[1:], lista2)
        else:
            return intercecao(lista1[1:], lista2)
    return retira_repetidos(gera_intercecao(lista1, lista2))


# C) intercala os numeros das listas
def intercala(lista1, lista2):
    if lista1 == []:
        if lista2 == []:
            return []
        else:
            return lista2
    elif lista2 == []:
        if lista1 == []:
            return []
        else:
            return lista1
    else:
        return [lista1[0]] + [lista2[0]] + intercala(lista1[1:], lista2[1:])