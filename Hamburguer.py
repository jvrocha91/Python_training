print("=========================================")
print("Bem vindo a hamburgueria Burguer do Joao!")
print("=========================================")
      
Name=input("Digite um nome de usuario:")
Conta=0
x=0


while True:

    print("----------------------------------")  
    print("\nQual produto deseja adicionar a sua compra:\n\n1-Hamburguer: 20.0 R$\n2-Batata: 10.0 R$\n3-Refrigerante: 8.0 RS")
    print("Digite '0' para encerrar o pedido\n")
    print("----------------------------------") 
    Cod=int(input("\nDigite um codigo de produto:"))

    if Cod==0:
        break

    if Cod==1:
        
        print("\nHamburguer adicionado")
        Conta=Conta+10.0
        x=x+1

        Option=int(input("\nDeseja Continuar o pedido ?\n\n1-Sim\n2-Nao\n"))

        if Option==2:
            break 
        if Option==1:
            continue 
    

    if Cod==2:
        
        print("\nBatatas fritas adicionadas")
        Conta=Conta+20.0
        x=x+1
            
        Option=int(input("\nDeseja Continuar o pedido ?\n\n1-Sim\n2-Nao\n"))

        if Option==2:
            break 
        if Option==1:
            continue 
         

    if Cod==3:
        print("\nRefrigerante adicionado")
        Conta=Conta+8.0
        x=x+1

        Option=int(input("\nDeseja Continuar o pedido ?\n\n1-Sim\n2-Nao\n"))

        if Option==2:
             break 
        if Option==1:
            continue     
        
            
while True:
    
    confirm=int(input(f"Sua compra tem {x} produto(s)\nDeseja confirmar pedido ?\n\n-Sim\n-Nao\n"))
            
    if confirm==1:
        break
    if confirm==2:
        print("\nRealize o pedido novamente")
        break
            
            
                  
print(f"\nA conta de {Name} sera de {Conta} Reais")      

        

        
              
