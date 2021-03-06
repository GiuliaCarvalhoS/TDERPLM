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
    i = 0
    resultado = []
    if conectivo1 == 'p' and conectivo2 == 'p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] or matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] and matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[0][i] or matriz[0][i]) and (not matriz[0][i] or matriz[0][i]))
                i += 1
    elif conectivo1 == '~p' and conectivo2 == '~p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or not matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] and not matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] or not matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[0][i] or not matriz[0][i]) and (matriz[0][i] or not matriz[0][i]))
                i += 1
    elif conectivo1 == '~p' and conectivo2 == 'p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] and matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] or matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[0][i] or matriz[0][i]) and (not matriz[0][i] or not matriz[0][i]))
                i += 1
    elif conectivo1 == 'p' and conectivo2 == '~p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] or not matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] and not matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or not matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[0][i] or not matriz[0][i]) and (matriz[0][i] or not matriz[0][i]))
                i += 1
    elif conectivo1 == 'p' and conectivo2 == 'q':
        tabela.append(sentenca)
        if implicacao == 'v':
            for c in matriz[0]:
                resultado.append(matriz[0][i] or matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] and matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[0][i] or matriz[1][i]) and (not matriz[1][i] or matriz[0][i]))
                i += 1
    elif conectivo1 == '~p' and conectivo2 == '~q':
        tabela.append(sentenca)
        if implicacao == 'v':
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or not matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] and not matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] or not matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[0][i] or not matriz[1][i]) and (matriz[1][i] or not matriz[0][i]))
                i += 1
    elif conectivo1 == '~p' and conectivo2 == 'q':
        tabela.append(sentenca)
        if implicacao == 'v':
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] and matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[0][i] or matriz[1][i]) and (not matriz[1][i] or not matriz[0][i]))
                i += 1
    elif conectivo1 == 'p' and conectivo2 == '~q':
        tabela.append(sentenca)
        if implicacao == 'v':
            for c in matriz[0]:
                resultado.append(matriz[0][i] or not matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[0][i] and not matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[0][i] or not matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[0][i] or not matriz[1][i]) and (matriz[1][i] or matriz[0][i]))
                i += 1
    elif conectivo1 == 'q' and conectivo2 == 'q':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] and matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[1][i] or matriz[1][i]) and (not matriz[1][i] or matriz[1][i]))
                i += 1
    elif conectivo1 == '~q' and conectivo2 == '~q':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or not matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] and not matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or not matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[1][i] or not matriz[1][i]) and (matriz[1][i] or not matriz[1][i]))
                i += 1
    elif conectivo1 == '~q' and conectivo2 == 'q':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] and matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[1][i] or matriz[1][i]) and (not matriz[1][i] or not matriz[1][i]))
                i += 1
    elif conectivo1 == 'q' and conectivo2 == '~q':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or not matriz[1][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] and not matriz[1][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or not matriz[1][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[1][i] or not matriz[1][i]) and (matriz[1][i] or matriz[1][i]))
                i += 1
    elif conectivo1 == 'q' and conectivo2 == 'p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] and matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[1][i] or matriz[0][i]) and (not matriz[0][i] or matriz[1][i]))
                i += 1
    elif conectivo1 == '~q' and conectivo2 == '~p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or not matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] and not matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or not matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[1][i] or not matriz[0][i]) and (matriz[0][i] or not matriz[1][i]))
                i += 1
    elif conectivo1 == '~q' and conectivo2 == 'p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] and matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((matriz[1][i] or matriz[0][i]) and (not matriz[0][i] or not matriz[1][i]))
                i += 1
    elif conectivo1 == 'q' and conectivo2 == '~p':
        if implicacao == 'v':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(matriz[1][i] or not matriz[0][i])
                i += 1
        elif implicacao == '^':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append([1][i] and not matriz[0][i])
                i += 1
        elif implicacao == '->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append(not matriz[1][i] or not matriz[0][i])
                i += 1
        elif implicacao == '<->':
            tabela.append(sentenca)
            for c in matriz[0]:
                resultado.append((not matriz[1][i] or not matriz[0][i]) and (matriz[0][i] or matriz[1][i]))
                i += 1

    matriz.append(resultado)
    return {"matriz": matriz, "tabela": tabela}


(exercio8(sentenca, conectivo1, implicacao, conectivo2, x, y))


def exibir(matriz, tabela):
    linha = 0
    for item in tabela:
        while linha < 5 :
            print(f"{item:<8}: {matriz[linha]}")
            linha += 1
            break


exibir(x, y)
