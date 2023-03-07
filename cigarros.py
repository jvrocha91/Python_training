nome=input("Digite o nome do usuario de cigarro:")
print("------------")

cigarros=int(input("Quantos cigarros o usuario utiliza por dia:"))

anos=int(input("A quantos anos o usuario fuma:"))
print("------------")      


tempo_perdido=(10*cigarros*anos*365)

tempo_perdido_dias=(tempo_perdido/1440)

print(f"{nome} ao todo perdeu {tempo_perdido_dias:4.2f} dias de vida com seu vicio em cigarros")
print("------------")   
                   
        
