# remoção
# usando del
# morte -> local conhecido -> morto desconhecido
lista=[5, 3, "a"]
print(lista)
del lista[2]
print(lista)

# usando pop
#morte ->  local conhecido -> morto conhecido
lista=[5, 3, "a"]
print(lista)
print(lista.pop(2))
print(lista)
