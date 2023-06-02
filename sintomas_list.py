def casdastro():
    nome=input("Digite o nome do paciente:")
    idade=int(input("Digite a idade do paciente:"))
    sintomas=[]
    for e in range(3):
        sintoma=input("Digite o sintoma:")
        sintomas.append(sintoma)
    
    return{"Nome":nome,"Sintomas": sintomas, "Idade": idade}

pacientes=[]
while True: 
    cadastrar = input("Deseja cadastrar um paciente? (S/N): ")
    if cadastrar =='n':
        break
    
    else:
        paciente = casdastro()
        pacientes.append(paciente)
        
# Listar os dados dos pacientes no console
print("Dados dos pacientes:")
for paciente in pacientes:
    print("----------------------------------")
    print("Nome:", paciente["Nome"])
    print("Sintomas:", ", ".join(paciente["Sintomas"]))
    print("Idade:", paciente["Idade"])
    print("----------------------------------")





    
    
 
    
    
    

    
        
    
    

    
    
    

     
    
    