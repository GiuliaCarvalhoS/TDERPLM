#class TabelaVerdade:

#def atribuicaoValoresTabela():
tabela = [["p" , "q", "~p", "~q", "p->q", "p^q","p v q", "p<->q"]]
matriz = [[True, True, False, False],
         [True, False, False, True],
         [False, True, True, False],
         [False, False, True, True]]

# nao a OU b
#def inplitcacaoPemQ(primeiroItem,):

primeiroItem4 = matriz[0][2] or matriz[0][1]
segundoItem4 = matriz[1][2] or matriz[1][1]
terceiroItem4 = matriz[2][2] or matriz[2][1]
quartoItem4 = matriz[3][2] or matriz[3][1]

#aqui tem q ver como add uma fileira na matriz pra ficar igual o doc dela no ex 4

#def inplitcacaoPeQ():

primeiroItem5 = matriz[0][0] and matriz[0][1]
segundoItem5 = matriz[1][0] and matriz[1][1]
terceiroItem5 = matriz[2][0] and matriz[2][1]
quartoItem5 = matriz[3][0] and matriz[3][1]

#aqui tem q ver como add uma fileira na matriz pra ficar igual o doc dela no ex 5

#def inplitcacaoPouQ():
primeiroItem6 = matriz[0][0] or matriz[0][1]
segundoItem6 = matriz[1][0] or matriz[1][1]
terceiroItem6 = matriz[2][0] or matriz[2][1]
quartoItem6 = matriz[3][0] or matriz[3][1]
#aqui tem q ver como add uma fileira na matriz pra ficar igual o doc dela no ex 6

#def inpitcacaoPouQ():
primeiroItem7 = ((matriz[0][2] or matriz[0][1]) and (matriz[0][3] or matriz[0][0]))
segundoItem7 = ((matriz[1][2] or matriz[1][1]) and (matriz[1][3] or matriz[1][0]))
terceiroItem7 = ((matriz[2][2] or matriz[2][1]) and (matriz[2][3] or matriz[2][0]))
quartoItem7 = ((matriz[3][2] or matriz[3][1]) and (matriz[3][3] or matriz[3][0]))
print(primeiroItem7)
print(segundoItem7)
print(terceiroItem7)
print(quartoItem7)
#aqui tem q ver como add uma fileira na matriz pra ficar igual o doc dela no ex 7