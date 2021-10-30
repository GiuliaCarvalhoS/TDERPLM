#Matriz os valores de p, q, ~p, ~q
def atribuicaoValoresTabela():
    tabela = ["p", "q", "~p", "~q"]
    matriz = [[True, True, False, False],
              [True, False, True, False],
              [False, False, True, True],
              [False, True, False, True]]

    return {"matriz": matriz, "tabela": tabela}

# "Instanciando" a matriz
matrizprincipal = atribuicaoValoresTabela()["matriz"]

# "Instanciando" a tabela
tabelaprincipal = atribuicaoValoresTabela()["tabela"]

#usuário digita a implicação
sentencaprincipal = input("Digite uma sentença: ").lower()

#implicação é transformada em lista para fazer sua manipulação
sentencadividida = list(sentencaprincipal)

#matriz que irá receber os valores que estiverem dentro dos parênteses
parenteses = []

#removendo os espaços que ficam ao usar o list()
for c in sentencadividida:
    if c == " ":
        sentencadividida.remove(c)
    

#encontrando a posição dos parênteses
pos1 = sentencadividida.index("(")
pos2 = sentencadividida.index(")")

#adicionando os valores que estão entre parênteses na matriz parenteses
for c in sentencadividida[pos1:(pos2 + 1)]:
    parenteses.append(c)

#removendo os parênteses da matriz parenteses
for c in parenteses:
    if c == "(" or c == ")":
        parenteses.remove(c)

#removendo a implicação que está dentro dos parênteses da sentença principal
del sentencadividida[pos1:(pos2 + 1)]


for j in parenteses:
    #verificando o tamanho da matriz parenteses
    if len(parenteses) == 4:  #tamanho igual a 4, significa que há uma negação (~) ou uma implicação (->)
        #verificnado se a negação está no primeiro conectivo
        if parenteses.index("~") == 0:
            parentesesconectivo1 = parenteses[0] + parenteses[1]
            parentesesimplicacao = parenteses[2]
            parentesesconectivo2 = parenteses[3]
            break
        #verificando se a negação está no segundo conectivo
        elif parenteses.index("~") == 2:
            parentesesconectivo1 = parenteses[0]
            parentesesimplicacao = parenteses[1]
            parentesesconectivo2 = parenteses[2] + parenteses[3]
            break
        #caso não haja negação na sentença, há então uma implicação (->)
        else:
            parentesesconectivo1 = parenteses[0]
            parentesesimplicacao = parenteses[2]
            parentesesconectivo2 = parenteses[3]
            break
    # tamanho igual a 5, significa que pode haver 2 negações (~) ou uma implicação (->) e uma negação ou uma bicondicionaç (<->)
    elif len(parenteses) == 5:
        
        if "~" in parenteses:
            # verificnado se há duas negações e se não há nenhuma implicação
            if parenteses.index("~") == 0 and parenteses.index(">") == -1:
                parentesesconectivo1 = parenteses[0] + parenteses[1]
                parentesesimplicacao = parenteses[2]
                parentesesconectivo2 = parenteses[3] + parenteses[4]
                break
            # verificnado se a negação no primeiro conectivo e uma implicação
            elif parenteses.index("~") == 0 and parenteses.index(">") > -1:
                parentesesconectivo1 = parenteses[0] + parenteses[1]
                parentesesimplicacao = parenteses[3]
                parentesesconectivo2 = parenteses[4]
                break
            # verificnado se a negação no segundo conectivo e uma implicação
            elif parenteses.index("~") == 3 and parenteses.index(">") > -1:
                parentesesconectivo1 = parenteses[0]
                parentesesimplicacao = parenteses[2]
                parentesesconectivo2 = parenteses[3] + parenteses [4]
                break
        #caso não encontre implicação ou negação, há então uma bicondicional
        else:
            
            parentesesconectivo1 = parenteses[0]
            parentesesimplicacao = parenteses[1]
            parentesesconectivo2 = parenteses[4]
            
            break
    # tamanho igual a 5, significa que pode haver 2 negações (~) e uma implicação (->) ou uma negação e uma bicondicional (<->)
    elif len(parenteses) == 6:
        #verificando se há duas negações e uma implicação
        if parenteses.index("~") == 0 and parenteses.index(">") > -1 and parenteses.index("<") == -1:
            parentesesconectivo1 = parenteses[0] + parenteses[1]
            parentesesimplicacao = parenteses[3]
            parentesesconectivo2 = parenteses[4] + parenteses[5]
            break
        #verificando se há uma negação no primeiro termo e uma bicondicional
        elif parenteses.index("~") == 0 and parenteses.index(">") > -1 and parenteses.index("<") > -1:
            parentesesconectivo1 = parenteses[0] + parenteses[1]
            parentesesimplicacao = parenteses[2]
            parentesesconectivo2 = parenteses[5]
            break
        #temos a presença de uma negação no segundo conectivo e de uma bicondicional
        else:
            parentesesconectivo1 = parenteses[0]
            parentesesimplicacao = parenteses[1]
            parentesesconectivo2 = parenteses[4] + parenteses [5]
            break
    # tamanho igual a 7, significa que há duas negações e uma bicondicional (<->)
    elif len(parenteses) == 7:
            parentesesconectivo1 = parenteses[0] + parenteses[1]
            parentesesimplicacao = parenteses[2]
            parentesesconectivo2 = parenteses[5] + parenteses[6]
            break
    else:
        parentesesconectivo1 = parenteses[0]
        parentesesimplicacao = parenteses[1]
        parentesesconectivo2 = parenteses[2]

#verificando a sentença que está fora do parenteses em relação aos conectivos
for i in sentencadividida:
    if i == "~":
        negacao = sentencadividida.index("~")
        sentencaconectivo1 = sentencadividida[negacao] + sentencadividida[negacao + 1]
    elif i == "p":
        sentencaconectivo1 = i
    elif i == "q":
        sentencaconectivo1 = i

#verificando a sentença que está fora do parenteses em relação as implicações

for c in sentencadividida:
    if c == "-":
        sentencadividida.remove(c)
    if c == "<":
        sentencaimplicacao = c

    elif c == ">":
        sentencaimplicacao = c
    elif c == "~":
        if len(sentencadividida) == 4:
            sentencaimplicacao = sentencadividida[3]
        else:
            sentencaimplicacao = sentencadividida[2]
    else:

        sentencaimplicacao = sentencadividida[0]


def exercicio9(sentenca,parenteses1, parentesesimplicacao, parenteses2, conectivo1, implicacao, matriz, tabela, pos1):
    i = 0
    j = 0
    resultadoparenteses = [] #recebe o resultado da sentença de dentro dos parênteses
    resultadofinal = [] #recebe o resultado final entre a sentaça de fora do parentêses e a de dentro dos parênteses

    if parenteses1 == "p" and parenteses2 == 'p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] and matriz[0][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((not matriz[0][i] or matriz[0][i]) and (not matriz[0][i] or matriz[0][i]))
                i += 1
    elif parenteses1 == "~p" and parenteses2 == 'p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] and matriz[0][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[0][i] or matriz[0][i]) and (not matriz[0][i] or not matriz[0][i]))
                i += 1
    elif parenteses1 == "~p" and parenteses2 == '~p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or not matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] and not matriz[0][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or not matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[0][i] or not matriz[0][i]) and (matriz[0][i] or not matriz[0][i]))
                i += 1
    elif parenteses1 == "p" and parenteses2 == 'q':
        
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] and matriz[1][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<':
            
            for c in matriz[0]:
                resultadoparenteses.append((not matriz[0][i] or matriz[1][i]) and (not matriz[1][i] or matriz[0][i]))
                i += 1
    elif parenteses1 == "p" and parenteses2 == '~q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] and not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((not matriz[0][i] or not matriz[1][i]) and (matriz[1][i] or not matriz[0][i]))
                i += 1
    elif parenteses1 == "~p" and parenteses2 == 'q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] and matriz[1][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[0][i] or matriz[1][i]) and (not matriz[1][i] or not matriz[0][i]))
                i += 1
    elif parenteses1 == "~p" and parenteses2 == '~q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] or not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[0][i] and not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[0][i] or not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[0][i] or not matriz[1][i]) and (matriz[1][i] or not matriz[0][i]))
                i += 1
    elif parenteses1 == "q" and parenteses2 == 'q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] and matriz[1][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] or matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((not matriz[1][i] or matriz[1][i]) and (not matriz[1][i] or matriz[1][i]))
                i += 1
    elif parenteses1 == "~q" and parenteses2 == '~q':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] or not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] and not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] or not matriz[1][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[1][i] or not matriz[1][i]) and (matriz[1][i] or not matriz[1][i]))
                i += 1
    elif parenteses1 == "q" and parenteses2 == 'p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] and matriz[0][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((not matriz[1][i] or matriz[0][i]) and (not matriz[0][i] or matriz[1][i]))
                i += 1
    elif parenteses1 == "~q" and parenteses2 == 'p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] and matriz[0][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] or matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[1][i] or matriz[0][i]) and (not matriz[0][i] or not matriz[1][i]))
                i += 1
    elif parenteses1 == "~q" and parenteses2 == '~p':
        if parentesesimplicacao == 'v':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] or not matriz[0][i])
                i += 1
        elif parentesesimplicacao == '^':
            for c in matriz[0]:
                resultadoparenteses.append(not matriz[1][i] and not matriz[0][i])
                i += 1
        elif parentesesimplicacao == '>':
            for c in matriz[0]:
                resultadoparenteses.append(matriz[1][i] or not matriz[0][i])
                i += 1
        elif parentesesimplicacao == '<':
            for c in matriz[0]:
                resultadoparenteses.append((matriz[1][i] or not matriz[0][i]) and (matriz[0][i] or not matriz[1][i]))
                i += 1
    #verifica se os parênteses vêm primeiro na sentença
    if pos1 == 0:
        if conectivo1 == "p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or matriz[0][j]) and
                                          (not matriz[0][j] or resultadoparenteses[j]))
                    j += 1
        elif conectivo1 == "~p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and not matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or not matriz[0][j]) and
                                          (matriz[0][j] or resultadoparenteses[j]))
                    j += 1
        elif conectivo1 == "q":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or matriz[1][j]) and
                                          (not matriz[1][j] or resultadoparenteses[j]))
                    j += 1
        else:
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and not matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or not matriz[1][j]) and
                                          (matriz[1][j] or resultadoparenteses[j]))
                    j += 1
    #verifica se os parênteses vêm no final da sentença
    else:
        if conectivo1 == "p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or matriz[0][j]) and
                                          (not matriz[0][j] or resultadoparenteses[j]))
                    j += 1
        elif conectivo1 == "~p":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and not matriz[0][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or not matriz[0][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or not matriz[0][j]) and
                                          (matriz[0][j] or resultadoparenteses[j]))
                    j += 1
        elif conectivo1 == "q":
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or matriz[1][j]) and
                                          (not matriz[1][j] or resultadoparenteses[j]))
                    j += 1
        else:
            if implicacao == "v":
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '^':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(resultadoparenteses[j] and not matriz[1][j])
                    j += 1
            elif implicacao == '>':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append(not resultadoparenteses[j] or not matriz[1][j])
                    j += 1
            elif implicacao == '<':
                tabela.append(sentenca)
                for c in matriz[0]:
                    resultadofinal.append((not resultadoparenteses[j] or not matriz[1][j]) and
                                          (matriz[1][j] or resultadoparenteses[j]))
                    j += 1
    #adiciona o resultado final na matriz principal
    matriz.append(resultadofinal)
    return {"matriz": matriz, "tabela": tabela}


exercicio9(sentencaprincipal, parentesesconectivo1, parentesesimplicacao, parentesesconectivo2,
           sentencaconectivo1, sentencaimplicacao, matrizprincipal, tabelaprincipal, pos1)


#função para exibir a tabela dos conectivos e implicações com os seus resultados
def exibir(matriz, tabela):
    linha = 0
    for item in tabela:
        while linha < 8:
            print(f"{item:<8}: {matriz[linha]}")
            linha += 1
            break


exibir(matrizprincipal, tabelaprincipal)
