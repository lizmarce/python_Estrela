#algoritmo de busca
#pesquisa sequencial

lista=[2,3,45,6,0]
valor_procurado=int(input("Valor procurado: "))
achou=False
k=0
while k < len(lista):
                    if lista[k]==valor_procurado:
                                        achou=True
                                        break
                    k+=1
# if preciso fazer teste lógico
# Se o teste lógico for verdadeiro executamos a instrução do if

if achou:
                    print(f"{valor_procurado} foi encontrado na posição {k+1}")
else:
                    print(f"{valor_procurado} não foi encontrado")
