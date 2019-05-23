# dado um tabuleiro e uma posicao verifica se essa posicao esta no tabuleiro
def esta_no_tab(x, y):
    if (0 < x < 9) and (0 < y < 9):
        return True
    else:
        return False

def pod_diag(x, y):
    if esta_no_tab(x + 1, y + 1) and esta_no_tab(x + 1, y - 1) and esta_no_tab(x - 1, y + 1) and esta_no_tab(x - 1, y - 1):
        return True
    else:
        return False

def pod_esq(x, y):
    if esta_no_tab(x - 1, y):
        return True
    else:
        return False

def pod_dir(x, y):
    if esta_no_tab(x + 1, y):
        return True
    else:
        return False

def pod_cima(x, y):
    if esta_no_tab(x, y + 1):
        return True
    else:
        return False

def pod_baix(x, y):
    if esta_no_tab(x, y - 1):
        return True
    else:
        return False

def tabuleiro(x, y):
    if esta_no_tab(x, y):
        if pod_diag(x, y):
            return 'Pode andar Todas as posicoes!!'
        elif pod_dir(x, y) and pod_cima(x, y) and pod_baix(x, y):
            return 'Nao anda para a esquerda nem na diagonal'
        elif pod_esq(x, y) and pod_cima(x, y) and pod_baix(x, y):
            return 'Nao anda para a direita nem na diagonal'
        elif pod_esq(x, y) and pod_dir(x, y) and pod_baix(x, y):
            return 'Nao anda para a cima nem na diagonal'
        elif pod_esq(x, y) and pod_dir(x, y) and pod_cima(x, y):
            return 'Nao anda para a baixo nem na diagonal'
        elif pod_esq(x, y) and pod_cima(x, y):
            return 'Nao anda para a direita nem para baixo nem nas diagonais'
        elif pod_dir(x, y) and pod_cima(x, y):
            return 'Nao anda para a esquerda nem para baixo nem nas diagonais'
        elif pod_esq(x, y) and pod_baix(x, y):
            return 'Nao anda para a direita nem para cima nem nas diagonais'
        else:
            return 'Nao anda para a esquerda nem para cima nem nas diagonais'
    else:
        return 'Posicao invalida!!'
