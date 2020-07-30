#número é par quando é divisível por 2 e o resto da divisão por 2 é 0
# n%2==0

#exibir os números pares entre 0 e um número digitado
#contadores-> são variáveis que são atualizadas com um valor constante
# por exemplo qpares=qpares+1, n=n+1,k=k+2
fim=int(input("Digite o último número: "))
n=0 # inicializar a variável
qpares=0
while n<=fim:
                    if n%2==0:
                                    print(n)
                                    qpares=qpares+1
                    n=n+1
print("Quantidade de pares", qpares)

#exercício com ímpares n%2==1 ou n%2=!0
