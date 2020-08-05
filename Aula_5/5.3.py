# função nativa range
# range com 1 parâmetro
#range(5) -> 5 números a partir do zero
for número in range(5):
                    print(número)
#
print()
#

# range com 2 parâmetros
# range(2,5) -> início=2; fim=5-1=4 e passo=1
for número in range(2,5):
                    print(número)
# Como print tem um pula linha embutido
# Se usarmos ele sem parâmetro então ele pula linha
print()
#
                    
# range com 2 parâmetros
# range(4,11,2) -> início=4; fim=11-1=10 e passo=2
# 4,6,8,10
for número in range(4,11,2):
                    print(número, end=" ")
# a função print tem embutida \n no fim
# end=" " serve para não pular linha
#
print()
#
print(list(range(7)))
#
print()
#
a=list(range(1,5))
print(a)
