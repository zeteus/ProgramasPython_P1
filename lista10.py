'''
Funcao auxiliar da funcao 'contarep' e 'jubila' que retorna uma lista somente com as materias reprovadas
'''
def list_nota_baixa(disciplina):
    '''
    Funcao auxiliar da questao '1' que retorna somente se a nota for menor que 5
    '''
    def nota_baixa(nota):
        return nota < 5

    if disciplina == []:
        return []
    elif nota_baixa(disciplina[0][2]):    
        return [disciplina[0]] + list_nota_baixa(disciplina[1:])
    else:
        return list_nota_baixa(disciplina[1:])

'''
    1) CALCULA O NUMERO DE REPROVACOES DE UM ALUNO
'''

'''
Funcao principal da questao '1' que conta a quantidade de reprovacoes
'''
def conterep(historico):
    return len(list_nota_baixa(historico[1]))


'''
    2) VERIFICAR SE UM ALUNO ESTA EM SITUACAO DE JUBILAMENTO
'''
'''
'''
def jubila(historico):
    def cria_lista_rep(list_rep):
        if list_rep == []:
            return []
        else:
            return [(list_rep[1][0], list_rep[1][2])] + cria_lista_rep(list_rep[1:])
    return cria_lista_rep(list_nota_baixa(historico[1]))
    



lista = ((2018,'CienciasComputacao',2018103811), [('prog1', (2019, 2), 7), ('Ed1', (2019, 2), 2), ('Eletrica', (2019, 2), 3)])
print (list_nota_baixa(lista[1]))
print (jubila(lista))