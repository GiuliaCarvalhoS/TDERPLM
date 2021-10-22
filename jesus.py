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
sentencadividida = list(sentenca)
parenteses = []

for c in sentencadividida:
    if c == " ":
        sentencadividida.remove(c)


pos1 = sentencadividida.index("(")
pos2 = sentencadividida.index(")")


for c in sentencadividida[pos1:(pos2 + 1)]:
    parenteses.append(c)

for c in parenteses:
    if c == "(" or c == ")":
        parenteses.remove(c)

del sentencadividida[pos1:(pos2 + 1)]

parentesesconectivo1 = parenteses[0]
parentesesimplicacao = parenteses[1]
parentesesconectivo2 = parenteses[2]


for i in sentencadividida:
    if i == "~":
        negacao = sentencadividida.index("~")
        setencaconectivo1 = sentencadividida[negacao] + sentencadividida[negacao + 1]
        break
    elif i == "p":
        setencaconectivo1 = i
        break
    elif i == "q":
        setencaconectivo1 = i
        break

for c in sentencadividida:
    match c:
        case "<":
            setencaimplicacao = c
            break
        case ">":
            setencaimplicacao = c
            break
        case "~":
            setencaimplicacao = sentencadividida[2]
            break
        case _:
            setencaimplicacao = sentencadividida[1]
            break




def exercicio9(sentenca,parenteses1, parentesesimplicacao, parenteses2, conectivo1, implicacao, matriz, tabela, pos1):
    i = 0
    j = 0
    resultado1 = []
    resultado = []
    if parenteses1 == "p" and parenteses2 == 'p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultado1.append(matriz[0][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultado1.append(matriz[0][i] and matriz[0][i])
                i += 1
        elif parentesesimplicacao == '->':
            for c in matriz[0]:
                resultado1.append(not matriz[0][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<->':
            for c in matriz[0]:
                resultado1.append((not matriz[0][i] or matriz[0][i]) and (not matriz[0][i] or matriz[0][i]))
                i += 1
    elif parenteses1 == "p" and parenteses2 == 'q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultado1.append(matriz[0][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultado1.append(matriz[0][i] and matriz[1][i])
                i += 1
        elif parentesesimplicacao == '->':
            for c in matriz[0]:
                resultado1.append(not matriz[0][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<->':
            for c in matriz[0]:
                resultado1.append((not matriz[0][i] or matriz[1][i]) and (not matriz[1][i] or matriz[0][i]))
                i += 1
    elif parenteses1 == "q" and parenteses2 == 'q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultado1.append(matriz[1][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultado1.append(matriz[1][i] and matriz[1][i])
                i += 1
        elif parentesesimplicacao == '->':
            for c in matriz[0]:
                resultado1.append(not matriz[1][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<->':
            for c in matriz[0]:
                resultado1.append((not matriz[1][i] or matriz[1][i]) and (not matriz[1][i] or matriz[1][i]))
                i += 1
    elif parenteses1 == "q" and parenteses2 == 'p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultado1.append(matriz[1][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultado1.append(matriz[1][i] and matriz[0][i])
                i += 1
        elif parentesesimplicacao == '->':
            for c in matriz[0]:
                resultado1.append(not matriz[1][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<->':
            for c in matriz[0]:
                resultado1.append((not matriz[1][i] or matriz[0][i]) and (not matriz[0][i] or matriz[1][i]))
                i += 1
    if pos1 == 0:
        if conectivo1 == "p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or matriz[0][j]) and (not matriz[0][j] or resultado1[j]))
                    j += 1
        elif conectivo1 == "~p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and not matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or not matriz[0][j]) and (matriz[0][j] or resultado1[j]))
                    j += 1
        elif conectivo1 == "q":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or matriz[1][j]) and (not matriz[1][j] or resultado1[j]))
                    j += 1
        else:
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and not matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or not matriz[1][j]) and (matriz[1][j] or resultado1[j]))
                    j += 1
    else:
        if conectivo1 == "p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or matriz[0][j]) and (not matriz[0][j] or resultado1[j]))
                    j += 1
        elif conectivo1 == "~p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '^':
                print('Inferno')
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and not matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or not matriz[0][j]) and (matriz[0][j] or resultado1[j]))
                    j += 1
        elif conectivo1 == "q":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or matriz[1][j]) and (not matriz[1][j] or resultado1[j]))
                    j += 1
        else:
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append(resultado1[j] and not matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                print(resultado1)
                for c in matriz[0]:
                    resultado.append(not resultado1[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultado.append((not resultado1[j] or not matriz[1][j]) and (matriz[1][j] or resultado1[j]))
                    j += 1
    matriz.append(resultado)
    return {"matriz": matriz, "tabela": tabela}

exercicio9(sentenca, parentesesconectivo1, parentesesimplicacao, parentesesconectivo2, setencaconectivo1, setencaimplicacao,x, y, pos1)


def exibir(matriz, tabela):
    linha = 0
    for item in tabela:
        while linha < 8:
            print(f"{item:<8}: {matriz[linha]}")
            linha += 1
            break


exibir(x, y)