def inserir():
    ht=int(input("Digite o numero de horas trabalhas:"))
    sh=int(input("Digite o salario/hora:"))
    tempoServico=int(input("Digite o tempo de servico(meses):"))
    nFilhos=int(input("Digite o numero de filhos:"))

    while True:
        estadoCivil = input("Digite o estado civil:\nS-Solteiro\nC-Casado\nD-Divorciado/Desquitado\nV-Viuvo").upper()
        if estadoCivil == 'S':
            estadoCivil = 'Solteiro'
        elif estadoCivil == 'C':
            estadoCivil = 'Casado'
        elif estadoCivil == 'D':
            estadoCivil = 'Divorciado'
        elif estadoCivil == 'V':
            estadoCivil = 'Viuvo'
        else:
            print("Valor invalido, digite novamente")
            continue
        break
    return ht, sh, tempoServico, nFilhos, estadoCivil

     

def salario(ht, sh, tempoServico, nFilhos, estadoCivil):
    # Cálculo do salário bruto
    sb = sh * ht

    # Cálculo do desconto do INSS
    descInss = 0
    if sb >= 1000 and sb < 3000:
        descInss = sb * 0.05
    if sb >= 3000 and sb < 5000:
        descInss = sb * 0.085
    if sb >= 5000:
        descInss = sb * 0.15

    # Cálculo do salário bruto ajustado INSS
    sbAjustado = sb - descInss

    # Cálculo do desconto do IR
    descIr = 0
    if sbAjustado >= 1500 and sbAjustado < 2500:
        descIr = sbAjustado * 0.05
    if sbAjustado >= 2500 and sbAjustado < 4500:
        descIr = sbAjustado * 0.15
    if sbAjustado >= 4500 and sbAjustado < 6500:
        descIr = sbAjustado * 0.225
    if sbAjustado >= 6500:
        descIr = sbAjustado * 0.275

    # Cálculo do abono por tempo de serviço
    abonoServico = 200
    if tempoServico >= 5 and tempoServico < 10:
        abonoServico = 200 + sb * 0.1
    if tempoServico >= 10 and tempoServico < 15:
        abonoServico = 200 + sb * 0.2
    if tempoServico >= 15:
        abonoServico = 200 + sb * 0.3

    # Cálculo do abono salário família
    abonoFilhoCivil = nFilhos * sb * 0.1
    if estadoCivil == 'C':
        abonoFilhoCivil = abonoFilhoCivil * 0.05
    if estadoCivil == 'D':
        abonoFilhoCivil = abonoFilhoCivil * 0.10
    if estadoCivil == 'V':
        abonoFilhoCivil = abonoFilhoCivil * 0.15

    # Cálculo do salário líquido
    sl = sb - descInss - descIr + abonoServico + abonoFilhoCivil

    return sb, descInss, descIr, sl, abonoServico, abonoFilhoCivil

def imprimir_salario(ht, sh, tempoServico, nFilhos, estadoCivil):
    sb, descInss, descIr, sl, abonoServico, abonoFilhoCivil = salario(ht, sh, tempoServico, nFilhos, estadoCivil)
    
    print("Salário Bruto: ", sb)
    print("Desconto INSS: ", descInss)
    print("Desconto IR: ", descIr)
    print("Salário Líquido: ", sl)
    print("Abono Serviço: ", abonoServico)
    print("Abono Filho Civil: ", abonoFilhoCivil)

def main():
    ht, sh, tempoServico, nFilhos, estadoCivil = inserir()
    imprimir_salario(ht, sh, tempoServico, nFilhos, estadoCivil)

# Garante que o código seja executado apenas se o arquivo for executado diretamente, e não quando importado como um módulo
if __name__ == "__main__":
    main()


