print("=========================================")
print("Bem vindo ao sistema Mercado+ !")
print("=========================================")



# Cadastro de senha
Cadastro=int(input("Digite uma senha numerica a ser cadastrada:")) 
Acesso=int(input("\nDigite sua senha:"))
x=0
itens=0


# Verificação da senha e acesso ao sistema
if Acesso==Cadastro:
    print("\nAcesso permitido")


    while True:
        
        # Menu de opções
        menu=int(input("\n\n----------------------------\n1-Registar saldo inicial disponivel\n2-Registrar venda\n3-Saldo do dia\n----------------------------\n\n"))


        # Registro do saldo inicial
        if menu == 1:
            saldo=float(input("Digite o valor do saldo atual disponivel no caixa:"))
            continue


        # Registro de venda
        elif menu == 2:
            x+=1
            valor_total=0
            valor_final=0
            while True:
                
                print(f"====REGISTRO DE VENDA : {x} ====")
                produto=input("Digite o nome do produto:")
                valor_produto=float(input("Digite o valor do produto:"))
                valor_total+=valor_produto
                itens+=1

                registro=int(input("\nDeseja continuar registro:\n1-SIM\n2-NAO\n"))
                if registro == 1:
                    continue
                if registro == 2:
                    print(f"O valor a ser pago e de : {valor_total} R$")
                    valor_pago=float(input("Digite o valor entregue pelo cliente:"))
                    troco=valor_pago - valor_total 
                    print(f"O troco deve ser de : {troco} R$")
                    saldo+=valor_total
                    valor_final+=valor_total
                    print(f"O saldo atual do caixa e de : {saldo}")
                    print("=======================")
                    break


        # Verificação do saldo do dia
        elif menu == 3:
            Acesso=int(input("\nDigite sua senha para checar saldo:"))

            if Acesso==Cadastro:
                print("\nAcesso permitido")
                print("\n=======================\n")
                print(f"O numero de vendas realizadas foi de {x}\n")
                print(f"O numero total de itens comercializados foi de {itens} itens\n")
                print(f"O valor total arrecadado no dia foi de {valor_final} R$\n")
                print(f"O saldo no caixa e de {saldo} R$\n")
                print("=======================")



            else:
                print("Acesso negado")
                continue
                


#Mensagem caso a senha de acesso esteja incorreta 
else:
    print("Acesso negado")
    

    
