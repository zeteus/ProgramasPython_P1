# verifica se um numero pertence ao intervalo [a,b]

def verifica_limites(a, b, c):
    if a < b:
        if a <= c <= b:
            return 'Pertence ao intervalo'
        else:
            return 'Nao pertence ao intervalo'
    else:
        aux = a
        a = b
        b = aux

        if a <= c <= b:
            return 'Pertence ao intervalo'
        else:
            return 'Nao pertence ao intervalo'