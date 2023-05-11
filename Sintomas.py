dados= [
    {"DOENCAS":"GRIPE", "SINTOMAS":["TOSSE","CORIZA","FEBRE","DOR MUSCULAR"]},
    {"DOENCAS":"DENGUE", "SINTOMAS":["FEBRE","DOR MUSCULAR"]},
    {"DOENCAS":"COVID", "SINTOMAS":["FEBRE","TOSSE","FALTA DE AR"]},
    {"DOENCAS":"MALARIA", "SINTOMAS":["FEBRE","CALAFRIO","MANCHA NO CORPO"]},
    ]

findoenca=input("DIGITE A DOENCA PROCURADA:  ")

flag=False
for i in dados:
    if i["DOENCAS"]==findoenca:
        print(i["SINTOMAS"])
        flag=True
            
        if flag==False:
            print("DOENCA NAO CADASTRADA")    