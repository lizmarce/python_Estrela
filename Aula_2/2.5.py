#Exemplo 5: Categorias de produto
# Categoria e preço
# 1 ->10, 2->18, 3->23, 4->26, 5->31
categoria=int(input("Digite a Categoria: \n"))
if categoria ==1:
                    preço=10
else:
                    if categoria==2:
                                        preço=18
                    else:
                                        if categoria==3:
                                                            preço=23
                                        else:
                                                            if categoria==4:
                                                                                preço=26
                                                            else:
                                                                                if categoria==5:
                                                                                                    preço=31
                                                                                else:
                                                                                                    print("Categoria inválida\nDigite um valor entre 1 e 5.")
                                                                                                    preço=0
print(f"O preço do produto é : R${preço: 5.2f}")
