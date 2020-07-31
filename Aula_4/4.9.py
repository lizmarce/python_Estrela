#adicionando elementos a uma lista
lista=[]
while True:
                    n=int(input("Digite um número ou 0 para sair"))
                    if n==0:
                                        break
                    lista.append(n)
k=0
while k<len(lista):
                    print(lista[k])
                    k+=1
