# Defina uma função que receba a indutância L e a
# capacitância C, e resulta na frequência
# de ressonância de um aparelho de rádio

# importa da biblioteca matematica a funcao raiz
from math import sqrt


# definir o numero pi por funcao
def pi():
    return 3.14


# funcao principal que calcula a frequencia
def freq_radio(L, C):
    return 1 / (2 * pi() * sqrt(L * C))

