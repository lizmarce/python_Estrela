#declarando lista
lista=[1,2.0, [3,4,6,7], "a", True]
print("lista=",lista)
#acessando elementos
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
#exibindo fatias
print(lista[0:2])
print(lista[2:5])
#acessando lista dentro de lista
print(lista[2][0])
#alterando elementos da lista
lista[1]="Boa Noite"
print(lista[1])
