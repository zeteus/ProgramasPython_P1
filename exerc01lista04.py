# Calcular o custo de energia em relacao ao salario minimo, com desconto de 15%

# funcao auxiliar para fazer o desconto de 15%
def desconto(valor):
    return valor * 0.15


# funcao que defrine o valor dos quilowatts
def valor_kW(salario, q):
    return (salario / 5) * q


# funcao principal que calcula o valor a ser pago
def valor_energia(salario, kW):
    return desconto((valor_kW(salario, kW)))

