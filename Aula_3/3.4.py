n=1
soma=0
k=int(input(f"Você quer calcular a média de quantos números? "))
while n<=k:
                    x=int(input(f"Digite o {n} número: "))
                    soma=soma+x
                    n=n+1
print(f"Média: {soma/k :5.2f}")
