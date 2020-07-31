#fila
#inclusão no fim e remoção no início
#FIFO
#Métodos -> append, del e pop

último=10
fila=list(range(1,último+1))
while True:
                    print(f"\nExistem {len(fila)} clientes na fila")
                    print(f" Fila atual: {fila}")
                    print("F ou A ou S")
                    operação=input("F ou A ou S")
                    if operação =="A":
                                            if len(fila)>0:
                                                                atendido=fila.pop(0)
                                                                print(f"Cliente {atendido} atendido")
                                            else:
                                                                print("Fila vazia!")
                    elif operação=="F":
                                        último+=1
                                        fila.append(último)
                    elif operação=="S":
                                        break
                    else:
                                        print("Operação Inválida")
                    
                        
