#Média->inserção+acessar+exibir
#Nota {k} -> texto+ variável
#notas[k] -> elemento da posição k da lista notas
notas = [0, 0, 0, 0, 0 ]
soma=0
k=0
while k< len(notas):
                    notas[k]=float(input(f"Notas{k}:")) #inserindo a nota na posição k
                    soma+=notas[k]
                    k+=1
#terminei a inserção das notas
# calculei a soma das notas
k=0
while k< len(notas):
                    print(f"Nota {k}:{notas[k]:6.2f}")
                    k+=1
print(f"Média: {soma/k:5.2}")
                    
