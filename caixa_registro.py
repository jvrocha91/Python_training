print("=========================================")
print("Bem vindo ao sistema Mercado+ !")
print("=========================================")

Cadastro=int(input("Digite uma senha numerica a ser cadastrada:")) 

Acess=int(input("\nDigite sua senha:"))
x=0

  

if Acess==Cadastro:
    print("\nAcesso permitido")

    while True:

        menu=int(input("\n--------------------\n1-Registar saldo inicial disponivel\n2-Registrar venda\n--------------------"))
        
        if menu == 1:
            saldo=float(input("Digite o valor do saldo atual disponivel no caixa:"))
            continue

        elif menu == 2:
            x+=1
            valor_total=0
            while True:
                
                print(f"====REGISTRO DE VENDA : {x} ====")
                produto=input("Digite o nome do produto:")
                valor_produto=float(input("Digite o valor do produto:"))
                valor_total+=valor_produto

                registro=int(input("\nDeseja continuar registro:\n1-SIM\n2-NAO"))
                if registro == 1:
                    continue
                if registro == 2:
                    print(f"O valor a ser pago e de : {valor_total} R$")
                    valor_pago=float(input("Digite o valor entregue pelo cliente:"))
                    troco=valor_pago - valor_total 
                    print(f"O troco deve ser de : {troco} R$")
                    saldo+=valor_total
                    print(f"O saldo atual do caixa e de : {saldo}")
                    print("=======================")
                    break
                
            
            
            
           
    






else:
    print("Acesso negado") 
    

    
