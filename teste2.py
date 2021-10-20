# class TabelaVerdade:
import collections


def atribuicaoValoresTabela():
    tabela = ["p", "q", "~p", "~q"]
    matriz = [[True, True, False, False],
              [True, False, True, False],
              [False, False, True, True],
              [False, True, False, True]]

    return {"matriz": matriz, "tabela": tabela}


# "Instanciando" a matriz
#x = atribuicaoValoresTabela()["matriz"]

# "Instanciando" a tabela
#y = atribuicaoValoresTabela()["tabela"]


# Operação a->b (Simplificando = não a OU b)
def pImplicaQ(matriz, tabela):
    primeiroItem4 = matriz[2][0] or matriz[1][0]  # Primeiro item de ~a OU b
    segundoItem4 = matriz[2][1] or matriz[1][1]  # Segundo item de ~a OU b
    terceiroItem4 = matriz[2][2] or matriz[1][2]  # Terceiro item de ~a OU b
    quartoItem4 = matriz[2][3] or matriz[1][3]  # Quarto item de ~a OU b

    # Adicionar o resultado na matriz recebida
    matriz.append([primeiroItem4, segundoItem4, terceiroItem4, quartoItem4])

    # Adicionar a operaçao na tabela
    tabela.append("p -> q")

    return {"matriz": matriz, "tabela": tabela}


# Operação a ^ b (a E b)
def pEQ(matriz, tabela):
    primeiroItem5 = matriz[0][0] and matriz[1][0]  # Primeiro item de a E b
    segundoItem5 = matriz[0][1] and matriz[1][1]  # Segundo item de a E b
    terceiroItem5 = matriz[0][2] and matriz[1][2]  # Terceiro item de a E b
    quartoItem5 = matriz[0][3] and matriz[1][3]  # Quarto item de a E b

    # Adicionar o resultado na matriz recebida
    matriz.append([primeiroItem5, segundoItem5, terceiroItem5, quartoItem5])

    # Adicionar a operaçao na tabela
    tabela.append("p ^ q")

    return {"matriz": matriz, "tabela": tabela}


# Operação a v b (a OU b)
def pOuQ(matriz, tabela):
    primeiroItem6 = matriz[0][0] or matriz[1][0]  # Primeiro item de a OU b
    segundoItem6 = matriz[0][1] or matriz[1][1]  # Primeiro item de a OU b
    terceiroItem6 = matriz[0][2] or matriz[1][2]  # Primeiro item de a OU b
    quartoItem6 = matriz[0][3] or matriz[1][3]  # Primeiro item de a OU b

    # Adicionar o resultado na matriz
    matriz.append([primeiroItem6, segundoItem6, terceiroItem6, quartoItem6])

    # Adicionar a operaçao na tabela
    tabela.append("p v q")

    return {"matriz": matriz, "tabela": tabela}


# Operação a <-> b (Simplificando: (NÃO a OU b) E (NÃO b OU a))
def pBicondicionalQ(matriz, tabela):
    primeiroItem7 = ((matriz[2][0] or matriz[1][0]) and (matriz[3][0] or matriz[0][0]))
    segundoItem7 = ((matriz[2][1] or matriz[1][1]) and (matriz[3][1] or matriz[0][1]))
    terceiroItem7 = ((matriz[2][2] or matriz[1][2]) and (matriz[3][2] or matriz[0][2]))
    quartoItem7 = ((matriz[2][3] or matriz[1][3]) and (matriz[3][3] or matriz[0][3]))

    # Adicionar o resultado na matriz
    matriz.append([primeiroItem7, segundoItem7, terceiroItem7, quartoItem7])

    # Adicionar a operaçao na tabela
    tabela.append("p <-> q")

    return {"matriz": matriz, "tabela": tabela}


#pImplicaQ(x, y)

#pEQ(x, y)

#pOuQ(x, y)

#pBicondicionalQ(x, y)

sentenca = input("Digite uma sentença: ").lower()
sentencadividida = sentenca.split()
conectivo1 = sentencadividida[0]
implicacao = sentencadividida[1]
conectivo2 = sentencadividida[2]


def exercio8(sentenca, conectivo1, implicacao, conectivo2, matriz, tabela):
    if conectivo1 == 'p' and conectivo2 == 'p':
        if implicacao == 'v':
            primeiroItem8 = matriz[0][0] or matriz[0][0]
            segundoItem8 = matriz[0][1] or matriz[0][1]
            terceiroItem8 = matriz[0][2] or matriz[0][2]
            quartoItem8 = matriz[0][3] or matriz[0][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[0][0] and matriz[0][0]
            segundoItem8 = matriz[0][1] and matriz[0][1]
            terceiroItem8 = matriz[0][2] and matriz[0][2]
            quartoItem8 = matriz[0][3] and matriz[0][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[2][0] or matriz[0][0]
            segundoItem8 = matriz[2][1] or matriz[0][1]
            terceiroItem8 = matriz[2][2] or matriz[0][2]
            quartoItem8 = matriz[2][3] or matriz[0][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[2][0] or matriz[0][0]) and (matriz[2][0] or matriz[0][0]))
            segundoItem8 = ((matriz[2][1] or matriz[0][1]) and (matriz[2][1] or matriz[0][1]))
            terceiroItem8 = ((matriz[2][2] or matriz[0][2]) and (matriz[2][2] or matriz[0][2]))
            quartoItem8 = ((matriz[2][3] or matriz[0][3]) and (matriz[2][3] or matriz[0][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == 'p' and conectivo2 == 'q':
        if implicacao == 'v':
            primeiroItem8 = matriz[0][0] or matriz[1][0]
            segundoItem8 = matriz[0][1] or matriz[1][1]
            terceiroItem8 = matriz[0][2] or matriz[1][2]
            quartoItem8 = matriz[0][3] or matriz[1][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[0][0] and matriz[1][0]
            segundoItem8 = matriz[0][1] and matriz[1][1]
            terceiroItem8 = matriz[0][2] and matriz[1][2]
            quartoItem8 = matriz[0][3] and matriz[1][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[2][0] or matriz[1][0]
            segundoItem8 = matriz[2][1] or matriz[1][1]
            terceiroItem8 = matriz[2][2] or matriz[1][2]
            quartoItem8 = matriz[2][3] or matriz[1][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[2][0] or matriz[1][0]) and (matriz[3][0] or matriz[0][0]))
            segundoItem8 = ((matriz[2][1] or matriz[1][1]) and (matriz[3][1] or matriz[0][1]))
            terceiroItem8 = ((matriz[2][2] or matriz[1][2]) and (matriz[3][2] or matriz[0][2]))
            quartoItem8 = ((matriz[2][3] or matriz[1][3]) and (matriz[3][3] or matriz[0][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == 'q' and conectivo2 == 'q':
        if implicacao == 'v':
            primeiroItem8 = matriz[1][0] or matriz[1][0]
            segundoItem8 = matriz[1][1] or matriz[1][1]
            terceiroItem8 = matriz[1][2] or matriz[1][2]
            quartoItem8 = matriz[1][3] or matriz[1][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[1][0] and matriz[1][0]
            segundoItem8 = matriz[1][1] and matriz[1][1]
            terceiroItem8 = matriz[1][2] and matriz[1][2]
            quartoItem8 = matriz[1][3] and matriz[1][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[3][0] or matriz[1][0]
            segundoItem8 = matriz[3][1] or matriz[1][1]
            terceiroItem8 = matriz[3][2] or matriz[1][2]
            quartoItem8 = matriz[3][3] or matriz[1][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[3][0] or matriz[1][0]) and (matriz[3][0] or matriz[1][0]))
            segundoItem8 = ((matriz[3][1] or matriz[1][1]) and (matriz[3][1] or matriz[1][1]))
            terceiroItem8 = ((matriz[3][2] or matriz[1][2]) and (matriz[3][2] or matriz[1][2]))
            quartoItem8 = ((matriz[3][3] or matriz[1][3]) and (matriz[3][3] or matriz[1][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == 'q' and conectivo2 == 'p':
        if implicacao == 'v':
            primeiroItem8 = matriz[1][0] or matriz[0][0]
            segundoItem8 = matriz[1][1] or matriz[0][1]
            terceiroItem8 = matriz[1][2] or matriz[0][2]
            quartoItem8 = matriz[1][3] or matriz[0][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[1][0] and matriz[0][0]
            segundoItem8 = matriz[1][1] and matriz[0][1]
            terceiroItem8 = matriz[1][2] and matriz[0][2]
            quartoItem8 = matriz[1][3] and matriz[0][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[3][0] or matriz[0][0]
            segundoItem8 = matriz[3][1] or matriz[0][1]
            terceiroItem8 = matriz[3][2] or matriz[0][2]
            quartoItem8 = matriz[3][3] or matriz[0][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[3][0] or matriz[0][0]) and (matriz[2][0] or matriz[1][0]))
            segundoItem8 = ((matriz[3][1] or matriz[0][1]) and (matriz[2][1] or matriz[1][1]))
            terceiroItem8 = ((matriz[3][2] or matriz[0][2]) and (matriz[2][2] or matriz[1][2]))
            quartoItem8 = ((matriz[3][3] or matriz[0][3]) and (matriz[2][3] or matriz[1][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == '~p' and conectivo2 == '~p':
        if implicacao == 'v':
            primeiroItem8 = matriz[2][0] or matriz[2][0]
            segundoItem8 = matriz[2][1] or matriz[2][1]
            terceiroItem8 = matriz[2][2] or matriz[2][2]
            quartoItem8 = matriz[2][3] or matriz[2][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[2][0] or matriz[2][0]
            segundoItem8 = matriz[2][1] or matriz[2][1]
            terceiroItem8 = matriz[2][2] or matriz[2][2]
            quartoItem8 = matriz[2][3] or matriz[2][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[0][0] or matriz[2][0]
            segundoItem8 = matriz[0][1] or matriz[2][1]
            terceiroItem8 = matriz[0][2] or matriz[2][2]
            quartoItem8 = matriz[0][3] or matriz[2][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[0][0] or matriz[2][0]) and (matriz[0][0] or matriz[2][0]))
            segundoItem8 = ((matriz[0][1] or matriz[2][1]) and (matriz[0][1] or matriz[2][1]))
            terceiroItem8 = ((matriz[0][2] or matriz[2][2]) and (matriz[0][2] or matriz[2][2]))
            quartoItem8 = ((matriz[0][3] or matriz[2][3]) and (matriz[0][3] or matriz[2][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == '~p' and conectivo2 == '~q':
        if implicacao == 'v':
            primeiroItem8 = matriz[2][0] or matriz[3][0]
            segundoItem8 = matriz[2][1] or matriz[3][1]
            terceiroItem8 = matriz[2][2] or matriz[3][2]
            quartoItem8 = matriz[2][3] or matriz[3][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[2][0] or matriz[3][0]
            segundoItem8 = matriz[2][1] or matriz[3][1]
            terceiroItem8 = matriz[2][2] or matriz[3][2]
            quartoItem8 = matriz[2][3] or matriz[3][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[0][0] or matriz[3][0]
            segundoItem8 = matriz[0][1] or matriz[3][1]
            terceiroItem8 = matriz[0][2] or matriz[3][2]
            quartoItem8 = matriz[0][3] or matriz[3][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[0][0] or matriz[3][0]) and (matriz[1][0] or matriz[2][0]))
            segundoItem8 = ((matriz[0][1] or matriz[3][1]) and (matriz[1][1] or matriz[2][1]))
            terceiroItem8 = ((matriz[0][2] or matriz[3][2]) and (matriz[1][2] or matriz[2][2]))
            quartoItem8 = ((matriz[0][3] or matriz[3][3]) and (matriz[1][3] or matriz[2][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == '~q' and conectivo2 == '~q':
        if implicacao == 'v':
            primeiroItem8 = matriz[3][0] or matriz[3][0]
            segundoItem8 = matriz[3][1] or matriz[3][1]
            terceiroItem8 = matriz[3][2] or matriz[3][2]
            quartoItem8 = matriz[3][3] or matriz[3][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[3][0] or matriz[3][0]
            segundoItem8 = matriz[3][1] or matriz[3][1]
            terceiroItem8 = matriz[3][2] or matriz[3][2]
            quartoItem8 = matriz[3][3] or matriz[3][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[1][0] or matriz[3][0]
            segundoItem8 = matriz[1][1] or matriz[3][1]
            terceiroItem8 = matriz[1][2] or matriz[3][2]
            quartoItem8 = matriz[1][3] or matriz[3][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[1][0] or matriz[3][0]) and (matriz[1][0] or matriz[3][0]))
            segundoItem8 = ((matriz[1][1] or matriz[3][1]) and (matriz[1][1] or matriz[3][1]))
            terceiroItem8 = ((matriz[1][2] or matriz[3][2]) and (matriz[1][2] or matriz[3][2]))
            quartoItem8 = ((matriz[1][3] or matriz[3][3]) and (matriz[1][3] or matriz[3][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    elif conectivo1 == '~q' and conectivo2 == '~p':
        if implicacao == 'v':
            primeiroItem8 = matriz[3][0] or matriz[2][0]
            segundoItem8 = matriz[3][1] or matriz[2][1]
            terceiroItem8 = matriz[3][2] or matriz[2][2]
            quartoItem8 = matriz[3][3] or matriz[2][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '^':
            primeiroItem8 = matriz[3][0] or matriz[2][0]
            segundoItem8 = matriz[3][1] or matriz[2][1]
            terceiroItem8 = matriz[3][2] or matriz[2][2]
            quartoItem8 = matriz[3][3] or matriz[2][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '->':
            primeiroItem8 = matriz[1][0] or matriz[2][0]
            segundoItem8 = matriz[1][1] or matriz[2][1]
            terceiroItem8 = matriz[1][2] or matriz[2][2]
            quartoItem8 = matriz[1][3] or matriz[2][3]
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
        elif implicacao == '<->':
            primeiroItem8 = ((matriz[1][0] or matriz[2][0]) and (matriz[0][0] or matriz[3][0]))
            segundoItem8 = ((matriz[1][1] or matriz[2][1]) and (matriz[0][1] or matriz[3][1]))
            terceiroItem8 = ((matriz[1][2] or matriz[2][2]) and (matriz[0][2] or matriz[3][2]))
            quartoItem8 = ((matriz[1][3] or matriz[2][3]) and (matriz[0][3] or matriz[3][3]))
            matriz.append([primeiroItem8, segundoItem8, terceiroItem8, quartoItem8])
            tabela.append(sentenca)
    x = atribuicaoValoresTabela()[matriz]
    y = atribuicaoValoresTabela()[tabela]
    print(x)
    print(y)
    return {"matriz": x, "tabela": y}


print(exercio8(sentenca, conectivo1, implicacao, conectivo2, , y))


def exibir(matriz, tabela):
    linha = 0

    for item in tabela:

        while linha < 8:
            print(f"{item:<8}: {matriz[linha]}")
            linha += 1
            break


exibir(x, y)
