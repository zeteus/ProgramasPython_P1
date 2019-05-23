# Calcular a area da figura (dividida em partes)

# define o numero pi
def pi():
    return 3,14

# funcao que calcula a area de um quadrado
def calcAreaQuad(x, y):
    return x * y

# funcao que calcula a area do semicirculo
def calcAreaSemiCirc(r):
    return (pi() * r * r) / 2

# funcao que calcula a area de um trapezio
def calcTrap(B, b, h):
    return (h * (B + b)) / 2

# funcao que calcula a area da figura dada
def calcArea(a, b, c, d):
    return calcAreaQuad(d, c) + calcAreaSemiCirc(d/2) + calcTrap(d, a, b)
