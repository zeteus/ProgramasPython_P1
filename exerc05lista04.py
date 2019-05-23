# funcao que calcula o valor de acordo com o numero de pessoas
def valor(p):
    try:
        if(p == 1):
            return 100
        elif(p == 2):
            return 130
        elif(p == 3):
            return 150
        elif(p == 4):
            return 165
        elif(p == 5):
            return 6
        elif(p == 6):
            return 180
        elif(p >= 7):
            return 185
        else:
            raise exception()
    except: pass


# funcao principal que passa o valor do retrato
def calcula_ret(pessoas, dia):
    try:
        if(dia == 'domingo' or dia == 'sabado'):
            return valor(pessoas) * 1.20
        elif(dia == 'segunda' or dia == 'terca' or dia == 'quarta' or dia == 'quinta' or dia == 'sexta'):
            return valor(pessoas)
        else:
            raise exception()
    except: pass

