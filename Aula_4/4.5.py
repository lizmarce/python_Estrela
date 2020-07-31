#Copiando Lista
#cópia da referência
lista1=[1,3,"A"]
print(lista1)
lista2=lista1 #copiando a referência -> mesmo endereço de memória
print(lista2)
lista1[0]="Eita"
print(lista1)
print(lista2)



#cópia do conteúdo
lista1=[1,3,"A"]
print(lista1)
lista2=lista1[:] #copiando os elementos -> endereços de memória diferente
print(lista2)
lista1[0]="Eita"
print(lista1)
print(lista2)
