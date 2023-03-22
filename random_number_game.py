import random

numeroComp=random.randint(0,100)

print("ADVINHE UM NUMERO DE 1 A 100")

tryhard=-1
x=0

while tryhard != numeroComp:

    try:
    
        tryhard=int(input("Digite um numero e tenta advinhar\nDigite '0' caso queia desistir:"))

        if tryhard == 0 :

            print("\nVoce desistiu do jogo\n")
            end=input("\nDeseja jogar novamente ? (S/N):")

            if end == "S" or "s":
                tryhard==numeroComp

            elif end== "N" or "n":
                break
            

        elif tryhard > numeroComp :
            print("\nO seu numero e maior do que o do computador")
            x+=1

        elif tryhard < numeroComp :
            print("\nO seu numero e menor do que o do computador")
            x+=1

        elif tryhard == numeroComp :
            print("\nPARABENS, VOCE ACERTOU")
            x+=1
            print(f"\nPara acertar voce teve {x} tentativas")

    except:
             print("Valor invalido, digite novamente")


        
                  
        
    
    
    


