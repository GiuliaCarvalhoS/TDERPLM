#class TabelaVerdade:


def atribuicaoValoresTabela():
  tabela = ["p" ,  "q",  "~p",  "~q"]
  matriz = [[True, True, False, False],
          [True, False, True, False],
          [False, False, True, True],
          [False, True, False, True]]

  return {"matriz": matriz, "tabela": tabela}

# "Instanciando" a matriz
x = atribuicaoValoresTabela()["matriz"]

# "Instanciando" a tabela
y = atribuicaoValoresTabela()["tabela"]


# Operação a->b (Simplificando = não a OU b)
def pImplicaQ(matriz, tabela):

  primeiroItem4 = matriz[2][0] or matriz[1][0] # Primeiro item de ~a OU b
  segundoItem4 = matriz[2][1] or matriz[1][1]  # Segundo item de ~a OU b
  terceiroItem4 = matriz[2][2] or matriz[1][2] # Terceiro item de ~a OU b
  quartoItem4 = matriz[2][3] or matriz[1][3]   # Quarto item de ~a OU b

  # Adicionar o resultado na matriz recebida
  matriz.append([primeiroItem4, segundoItem4, terceiroItem4, quartoItem4])

  # Adicionar a operaçao na tabela
  tabela.append("p -> q")
  
  return {"matriz": matriz, "tabela": tabela}

# Operação a ^ b (a E b)
def pEQ(matriz, tabela):
  primeiroItem5 = matriz[0][0] and matriz[1][0] # Primeiro item de a E b
  segundoItem5 = matriz[0][1] and matriz[1][1]  # Segundo item de a E b
  terceiroItem5 = matriz[0][2] and matriz[1][2] # Terceiro item de a E b
  quartoItem5 = matriz[0][3] and matriz[1][3]   # Quarto item de a E b

  # Adicionar o resultado na matriz recebida
  matriz.append([primeiroItem5, segundoItem5, terceiroItem5, quartoItem5])

  # Adicionar a operaçao na tabela
  tabela.append("p ^ q")

  return {"matriz": matriz, "tabela": tabela}



# Operação a v b (a OU b)
def pOuQ(matriz, tabela):
  primeiroItem6 = matriz[0][0] or matriz[1][0] # Primeiro item de a OU b
  segundoItem6 = matriz[0][1] or matriz[1][1]  # Primeiro item de a OU b
  terceiroItem6 = matriz[0][2] or matriz[1][2] # Primeiro item de a OU b
  quartoItem6 = matriz[0][3] or matriz[1][3]   # Primeiro item de a OU b

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


pImplicaQ(x, y)

pEQ(x, y)

pOuQ(x,y)

pBicondicionalQ(x, y)



# def exibir(matriz, tabela):
  
#   for item in tabela:
      
#     for linha in range(8):
#       print(f"{item:<8}: {matriz[linha]}")  
#       linha += 1
#       break
     
      

# exibir(x, y)





def exibir(matriz, tabela):
  linha=0
  
  for item in tabela:

    while linha < 8:
      print(f"{item:<8}: {matriz[linha]}")  
      linha += 1
      break

      
   
      

exibir(x, y)

#def exibirMAtriz(matriz):
  #for linha in matriz:
    #print(linha)
  
  
# #exibirMAtriz(x)


# variavelUnica = input("Digite uma implicação com dois conectivos: ")

# if variavelUnica.find("->") != -1:
 
#   seta = variavelUnica.split("->")
#   print
  
  
    
# seta = variavelUnica.split("->")
# # duoSeta= variavelUnica.split("<->")
# # sinalE= variavelUnica.split("v")
# # sinalOu= variavelUnica.split("^")
# # print(seta)







def implication (conective1, conective2, matriz = x, table=y):
	p=0
	q=1
	Np=2
	Nq=3
	result=[]
  

  
	
	result1=	matriz[0]

	result2=	matriz[1]
  
  if result1[0] == result2[0]:
    result.append(True)

  elif result1[1] == result2[1]:
    result.append(True)

  elif result1[2] == result2[2]:
    result.append(True)

  elif result1[3] == result2[3]:
    result.append(True)
  else:
    result.append(False)
    

	return result

resultado = implication("p","q")

print(resultado)

