# classifica em qual quadrante esta um ponto

def origem():
    return 'Este ponto esta na origem'

def quad_1():
    return 'Este ponto esta no primeiro quadrante'

def quad_2():
    return 'Este ponto esta no segundo quadrante'

def quad_3():
    return 'Este ponto esta no terceiro quadrante'

def quad_4():
    return 'Este ponto esta no quarto quadrante'

def ordenadas():
    return 'Este ponto esta no eixo das ordenadas'

def absissas():
    return 'Este ponto esta no eixo das absissas'

def pert_quad(x, y):
    if (x > 0) and (y > 0):
        return quad_1()
    elif (x < 0) and (y > 0):
        return quad_2()
    elif (x < 0) and (y < 0):
        return quad_3()
    elif (x > 0) and (y > 0):
        return quad_4()
    elif (x == 0) and (y != 0):
        return ordenadas()
    elif (x != 0) and (y == 0):
        return absissas()
    elif (x == 0) and (y == 0):
        return origem()
