ultimo=10
fila=list(range(1, ultimo+1))


while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}\n")
    print("-------------")
    print("Digite F para adicionar cliente ao fim da fila\nDigite A para realizar o atendimento\nDigite S para sair")
    operacao=input("Operacao(F,A ou S):")
    print("-------------")

    if operacao=="S" or operacao=="s":
        break

    if operacao=="A" or operacao=="a":
        if len(fila) > 0:
            atendido=fila.pop(0)
            print(f"\nCliente {atendido} atendido")
        else:
            print("\nFila vazia! Ninguem para atender")

    if operacao=="F" or operacao=="f":
        ultimo+=1
        fila.append(ultimo)

    else:
        print("\nOperacao invalida, digite apenas F,A ou S")
        

                 
