# função nativa enumerate
# cria -> tupla -> lista -> posição fixa
# [(0, lista[0]),...(k, lista[k]) ]

refrigerantes=["Coca", "Pepsi", "Tubaína", "Guaraná"]
print(refrigerantes)
print(list(enumerate(refrigerantes)))
print(list(enumerate(refrigerantes,start=1)))
print(list(enumerate(refrigerantes,start=2)))

#
print()
#
#fazer enumerate com o for
refrigerantes=["Coca", "Pepsi", "Tubaína", "Guaraná"]
k=0
for nome in refrigerantes:
                    print(f"[{k}]{nome}")
                    k+=1
# onde k é a posição do elemento


#
print()
#

refrigerantes=["Coca", "Pepsi", "Tubaína", "Guaraná"]
for posição, nome in enumerate(refrigerantes):
                    print(f"[{posição}]{nome}")
                   
