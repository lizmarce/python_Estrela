# estrutura de iterativa -> for
# percorro os elementos da lista
# sintaxe elemento in lista
# elemento foi um nome qualquer
# lista é o nome da lista que você quer percorrer
# não faço teste lógico

lista=[2, 4, 8]
for elemento in lista:
                    print(elemento)
# print() vazio pulo linha
print()
#
# mesmo programa com while
lista=[2, 4, 8]

# k é posição dos elementos da lista
# faço teste lógico
k=0
# começamos por zero pois é a primeira posição dos elementos da lista
while k<len(lista):
                    print(lista[k])
                    k+=1
