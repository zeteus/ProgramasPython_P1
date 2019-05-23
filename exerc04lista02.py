#Calcular a area de cada figura

#importar da biblioteca matematica
from math import sqrt


# define o numero pi
def pi():
    return 3,14


# funcao auxiliar para encontrar altura de um triangulo isoceles
def calcAltura(x, y):
    return sqrt((x * x) + ((y/2) * (y/2)))


# funcao auxiliar que calcula a area de um quadrado
def calcAreaQuad(x, y):
    return x * y


# funcao auxiliar que calcula a area do semicirculo
def calcAreaSemiCirc(r):
    return (pi() * r * r) / 2


# 9.1 area de um triangulo isoceles
# Entradas:
#   a = lado repetido do triangulo isoceles
#   b = base do triangulo isoceles
def calcArea1(a, b):
    return (calcAltura(a, b) * b) / 2


# 9.2 area de um triangulo isoceles junto com um semicirculo
# 9.3 area de uma casinha
# Entradas:
#   a = lado repetido do triangulo isoceles
#   b = base do triangulo isoceles e o raio do semicirculo
def calcArea2(a, b):
    return calcArea1(a, b) + calcAreaSemiCirc(b/2)


# 9.3 area de uma casinha
# Entradas:
#   a = lado repetido do triangulo isoceles
#   b = base do triangulo isoceles e do retangulo
#   c = lado do retangulo
def calcArea3(a, b, c):
    return calcArea1(a, b) + calcAreaQuad(b, c)


# 9.4 area de uma casinha
# Entradas:
#   a = lado repetido do triangulo isoceles
#   b = base do triangulo isoceles
#   c = base do retangulo
#   d = lado do retangulo
def calcArea4(a, b, c, d):
    return calcAreaQuad(c, d) - calcArea1(a, b)
