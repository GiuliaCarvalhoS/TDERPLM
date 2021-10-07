 #class TabelaVerdade:
V = True
F = False
#def atribuicaoValoresTabela:
matriz=[["p" , "q", "~p", "~q"],
[V, V, F, F],
[V, F, F, V],
[F, V, V, F],
[F, F, V, V]]
#nao a OU b
#def inpitcacaoPemQ:
primeiroItem = matriz[1][2] or matriz[1][1]
segundoItem = matriz[2][2] or matriz[2][1]
terceiroItem = matriz[3][2] or matriz[3][1]
quartoItem = matriz[4][2] or matriz[4][1]

print(primeiroItem)

