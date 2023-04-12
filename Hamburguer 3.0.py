ultimo=5
fila=list(range(1, ultimo+1))
Conta=0
x=0
soma=0
pago=[]



cardapio = {
    1: {"item": "Hamburguer", "preco": 20.0},
    2: {"item": "Batata", "preco": 10.0},
    3: {"item": "Batata com cheddar e bacon", "preco": 16.0},
    4: {"item": "Refrigerante", "preco": 8.0},
    5: {"item": "Suco natural", "preco": 7.0},
    6: {"item": "Sorvete", "preco": 11.0}
   
}



print("=========================================")
print("Bem vindo a hamburgueria Burguer do Joao!")
print("=========================================")
          

Cadastro=int(input("Digite uma senha numerica a ser cadastrada:")) 

Acess=int(input("\nDigite sua senha:")) 

  

if Acess==Cadastro: 

    print("\nAcesso permitido")

    while True:
        print(f"\nExistem {len(fila)} clientes na fila")
        print(f"Fila atual: {fila}\n")
        print("-------------")
        print("Digite F para adicionar cliente ao fim da fila\nDigite A para realizar o atendimento\nDigite S para sair")
        operacao=input("Operacao(F,A ou S):")
        print("-------------")
        

        if operacao=="S" or operacao=="s":
            Acess=int(input("\nDigite sua senha para checar o lucro do dia:"))

            if Acess==Cadastro:

                print(f"O lucro do dia foi de {soma} reais")
                print(f"\nOs atendimento foi(cliente-lucro):{pago}")
                break

            else:
                print("Acesso invalido")
                break
                    

        elif operacao=="F" or operacao=="f":
            ultimo+=1
            fila.append(ultimo)
            

        elif operacao=="A" or operacao=="a":
            if len(fila) > 0:
                atendido=fila.pop(0)
                print(f"\nCliente {atendido} sendo atendido:\n")

                while True:

                        print("----------------------------------")  
                        print("\nQual produto deseja adicionar a sua compra:\n")
                        for codigo,produto in cardapio.items():
                            print(f"{codigo}-{produto['item']}: {produto['preco']} R$")
                        print("Digite '0' para encerrar o pedido\n")
                        print("----------------------------------")
                        
                        Cod=int(input("\nDigite um codigo de produto:"))

                        if Cod==0:
                            break

                        if Cod in cardapio:
                            produto = cardapio[Cod]
                            print(f"\n{produto['item']} adicionado")
                            Conta+=produto['preco']
                            x+=1

                        Option = int(input("\nDeseja Continuar o pedido ?\n\n1-Sim\n2-Nao\n"))

                        if Option == 2:
                            break 
                        if Option == 1:
                            continue 
                        else:
                            print("Código inválido, por favor, tente novamente.")    


                        
                while True:
    
                        confirm=int(input(f"Sua compra tem {x} produto(s)\nDeseja confirmar pedido ?\n\n-Sim\n-Nao\n"))
                                
                        if confirm==1:
                            soma+=Conta
                            x=0
                            break
                        if confirm==2:
                            print("\nRealize o pedido novamente")
                            break
                                
            
                  
                print(f"\nA conta de cliente {atendido} sera de {Conta} Reais")
                pago.append(f"{atendido}-{Conta}R$\n")
                Conta=0
                            


                
            else:
                print("\nFila vazia! Ninguem para atender")

        else:
            print("\nOperacao invalida, digite apenas F,A ou S")

else: 

    print("Acesso negado") 
