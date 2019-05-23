# Calcular a compressao e a energia potencial armazenada em uma mola

# funcao que calcula a compressao da mola dada a forca e a constante da mesma
def compressao_mola(F, k):
    return F / k


# funcao que calcula a energia potencial armazenada na mola
def energia_potencial(k, x):
    return (k * x * x) / 2


# funcao principal
def forca_mola(F, k):
    print('COMPRESSAO DA MOLA:\n', compressao_mola(F, k))
    print('ENERGIA POTENCIAL ARMAZENADA:')
    return energia_potencial(k, compressao_mola(F, k))

