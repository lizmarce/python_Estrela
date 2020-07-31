
#ler, armazenar e escolher
números=[0, 0, 0, 0, 0]
k=0
while k<len(números):
                    números[k]=int(input(f" Números {k+1}:"))
                    k+=1
while True:
                    escolhido=int(input("Que posição você quer imprimir? (0 para sair)"))
                    if escolhido==0:
                                        break
                    print(f"Você escolheu o número:{números[escolhido -1]}")



###############          
#k=0
#while k<len(números):
#                    números=int(input(f" Números {k+1}:"))
#                  k+=1
#while True:
#                   escolhido=int(input("Que posição você quer imprimir? (0 para sair)")
#                   if k==0:
#                                        break
#                   print(f"Você escolheu o número:{números[k -1]}")
