# dado um retangulo printar em quais quadrantes

def origem():
    return 0

def quad_1():
    return 1

def quad_2():
    return 2

def quad_3():
    return 3

def quad_4():
    return 4

def pert_quad(x, y):
    if (x > 0) and (y > 0):
        return quad_1()
    elif (x < 0) and (y > 0):
        return quad_2()
    elif (x < 0) and (y < 0):
        return quad_3()
    elif (x > 0) and (y > 0):
        return quad_4()
    elif (x == 0) and (y == 0):
        return origem()

def quad(x1, y1, x2, y2):

    ponto1 = pert_quad(x1, y1)
    ponto2 = pert_quad(x2, y2)

    if ponto1 == 1 and ponto2 == 1:
        return 'Esta somente no primeiro quadrante'
    elif ponto1 == 2 and ponto2 == 2:
        return 'Esta somente no segundo quadrante'
    elif ponto1 == 3 and ponto2 == 3:
        return 'Esta somente no terceiro quadrante'
    elif ponto1 == 4 and ponto2 == 4:
        return 'Esta somente no quarto quadrante'
    elif (ponto1 == 1 and ponto2 == 2) or (ponto1 == 2 and ponto2 == 1):
        return 'Esta no primeiro e no segundo quadrante'
    elif (ponto1 == 3 and ponto2 == 4) or (ponto1 == 4 and ponto2 == 3):
        return 'Esta no terceiro e no quarto quadrante'
    elif (ponto1 == 2 and ponto2 == 3) or (ponto1 == 3 and ponto2 == 2):
        return 'Esta no segundo e no terceiro quadrante'
    elif (ponto1 == 1 and ponto2 == 4) or (ponto1 == 4 and ponto2 == 1):
        return 'Esta no primeiro e no quarto quadrante'
    elif (ponto1 == 1 and ponto2 == 3) or (ponto1 == 3 and ponto2 == 1) or (ponto1 == 2 and ponto2 == 4) or (ponto1 == 4 and ponto2 == 2):
        return 'Esta em todos os quadrantes'
    else:
        return 'Nao eh um retangulo'
