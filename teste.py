def atribuicaoValoresTabela():
    tabela = ["p", "q", "~p", "~q"]
    matriz = [[True, True, False, False],
              [True, False, True, False],
              [False, False, True, True],
              [False, True, False, True]]

    return {"matriz": matriz, "tabela": tabela}

# "Instanciando" a matriz
x = atribuicaoValoresTabela()["matriz"]

# "Instanciando" a tabela
y = atribuicaoValoresTabela()["tabela"]

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
    return {"matriz": matriz, "tabela": tabela}

exercio8(sentenca, conectivo1, implicacao, conectivo2,x , y)


def exibir(matriz, tabela):
    linha = 0

    for item in tabela:

        while linha < 8:
            print(f"{item:<8}: {matriz[linha]}")
            linha += 1
            break

exibir(x,y)