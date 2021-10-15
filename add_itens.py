
def implication (conective1, conective2, matriz = matriz, table=tabela):
	p=0
	q=1
	Np=2
	Nq=2
	result=[]
	
	result1=	matriz[conective1]
	result2=	matriz[conective2]

	for i in result1:
		for l in  result2:
		 if(i==l):
			 result.append(true)
		 else:
			 resul.append(false)

	return result


resultado = implication("p","q")

print(resultado)