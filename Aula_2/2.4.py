#Conta de telefone
#  <200 minutos R$0.20 por minuto
# 200<=minutos<=400 R$0.18 por minuto
# minutos>400 minutos R$0.15 por minuto
#posso fazer esse código com 3if's -> exercício

minutos=int(input("Quantos minutos foram utilizados esse mês: \n"))
if minutos<200:
                    preço=0.2
else:
                    if minutos <=400:
                                    preço=0.18
                    else:
                                        preço=0.15
print(f"O valor da conta é: R${minutos*preço:7.2f}")
