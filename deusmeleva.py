from typing import List, Any

import numpy
sentenca = input("Digite uma sentença: ").lower()
sentencadividida: list[Any] = list(sentenca)

for c in sentencadividida:
    if c == " ":
        sentencadividida.remove(c)
lista = numpy.ndarray(sentencadividida)
print(lista.find("("))
print(lista.find(")"))



