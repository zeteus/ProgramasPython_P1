# Calcule a area de um triangulo dados os lados A, B, C

# importa da biblioteca matematica a funcao raiz
from math import sqrt


# Pela lei dos cossenos
def cosseno(a, b, c):
    return (b * b + c * c - a * a) / (2 * b * c)


# Pela relacao fundamental da trigonometria
def seno(a, b, c):
    return sqrt(1 - cosseno(a, b, c) * cosseno(a, b, c))


# Pela definicao de seno
def altura(a, b, c):
    return b * seno(a, b, c)


# Pela definicao de area de um trianguulo
def area_triangulo(a, b, c):
    return (c * altura(a, b, c)) / 2

