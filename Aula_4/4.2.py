#Média -> acesso
#soma+=notas[k]  -> soma=soma+=notas[k]
#notas[k] elemento da posição k da lista nota
#k+-1 --> k=k+1

#k=0
#0<6? V
#soma=0+notas[0]
#soma=0+5
#soma=5
#k=0+1
#k=1
#1<6? V
#soma=5+notas[1]
#soma=5+2
#soma=7

notas=[5, 2, 8, 7, 9, 0]
soma=0
k=0
while k<len(notas):
                    soma+=notas[k]
                    k+=1
print(f"Média: {soma/len(notas):5.2f}")


                    
