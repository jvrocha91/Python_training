print("-------------")
print("Bem vindo a Seguradora Tabajata Ltda")
print("-------------")
print("Digite as informacoes solicitadas para que possamos calcular o ")
print("valor do seguro e das parcelas a serem pagas")
print("-------------")

VBS=float(input("Valor do bem a ser segurado:")) #Valor bruto do seguro
USER=int(input("Numero de usuarios:")) #Adicional por usuario
TS=int(input("Taxa de seguro:")) #Descontos 
DS=int(input("Taxa de desconto:")) #Valor liquido do seguro
NP=int(input("Numero de parcelas:")) #Valor das parcelas 

VSEG=VBS*TS/100 #Calcular o valor bruto do seguro
VUSER=VSEG*USER/100 #Calcular o valor adicional por usuario
DESC=(VSEG+VUSER)*DS/100 #Calcular os descontos
SEG=VSEG+VUSER-DESC #Calcular o valor liquido do seguro
VPARCELA=SEG/NP #Calcular o valor das parcelas



print("-------------")
print(f"O valor bruto do seguro e de {VSEG} reais")
print(f"O valor adicional sera de {VUSER} reais por usuario")
print(f"Os descontos serao de {DESC} reais")  
print("-------------")
print(f"O valor liquido do seguro e de {SEG} reais")
print(f"O valor das parcelas a serem pagas sao de {VPARCELA} reais em {NP} parcelas")
print("-------------")



       
            

        

