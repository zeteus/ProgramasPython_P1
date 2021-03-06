'''
* * * * * * * * * * * * * * * * * * * * *
* NOME:                                 *
*     > EZEQUIEL SCHNEIDER REINHOLTZ    *
*     > LUANA GABRIELE DE SOUSA COSTA   *
*                                       *
* PROFESSORA:                           *
*     > JORDANA SARMENGHI SALAMON       *
*                                       *
* MATERIA:                              *
*     > PROGRAMACAO 1 - 2019/01         *
*                                       *
* CURSO:                                *
*     > CIENCIA DA COMPUTACAO           *
*                                       *
* TRABALHO:                             *
*     > ROBOZIN DO SAMU                 *
*                                       *
* * * * * * * * * * * * * * * * * * * * *
'''

'''IMPORTACAO DE FUNCOES'''
from math import sqrt
from functools import reduce

'''==============================================================================================================''
* * * * * *
* PARTE A *
* * * * * *
'''

'''
FUNCAO AUXILIAR DE QUESTAO A PARAMETRICA:
OBJETIVO: Funcao que retorna a coordenada 'X' de um ponto
INPUTS: Uma Tupla 'p' para um ponto
OUTPUT: Retorna o primeiro elemento da Tupla
'''
def returnXpoint(p):
    return p[0]


'''
FUNCAO AUXILIAR DE QUESTAO A PARAMETRICA:
OBJETIVO: Funcao que retorna a coordenada 'Y' de um ponto
INPUTS: Uma Tupla 'p' para um ponto
OUTPUT: Retorna o segundo elemento da Tupla
'''
def returnYpoint(p):
    return p[1]


'''
FUNCAO AUXILIAR DE QUESTAO A PARAMETRICA:
OBJETIVO: Funcao que calcula e retorna a distancia entre dois pontos
INPUTS: Uma Tupla 'p1' para o primeiro ponto, Uma Tupla 'p2' para o segundo ponto
OUTPUT: Retorna a distancia entre os pontos de entrada
'''
def distPoint(p1, p2):
    return sqrt((returnXpoint(p1) - returnXpoint(p2)) ** 2 + (returnYpoint(p1) - returnYpoint(p2)) ** 2)


'''
FUNCAO AUXILIAR DE QUESTAO A PARAMETRICA:
OBJETIVO: Funcao que soma os valores de uma lista
INPUTS: Uma Lista 'l' para os numeros a serem somados
OUTPUT: Retorna o somatoria da lista de entrada
'''
def somatorio(lista):
    '''
    FUNCAO AUXILIAR DE SOMATORIO PARAMETRICA:
    OBJETIVO: Somar dois numeros de entrada
    INPUTS: Uma Variavel 'n1' para numero 1 e uma Variavel 'n2' para numero 2
    OUTPUT: Retorna a soma
    '''
    def somaNum(n1, n2):
    return n1 + n2
    
    return reduce(soma, lista)

'''
FUNCAO PRINCIPAL DA QUESTAO A:
OBJETIVO: Calcula a distancia percorrida por um robo especifico
INPUTS: Uma Lista 'l' com as informacoes do robo
OUTPUT: Retorna a distancia percorrida
'''

'''==============================================================================================================''
* * * * * *
* PARTE B *
* * * * * *
'''

'''
FUNCAO AUXILIAR DE QUESTAO B PARAMETRICA:
OBJETIVO: Funcao que mostra o robo que percorreu a maior distancia
INPUTS: a definir
OUTPUT: A distancia e o ID do robo "mais cansado"
'''
def robotMostTired(lista):
    ## a definir essa funcao
    return 1;