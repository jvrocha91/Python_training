MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 7.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 12.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0

def print_resources():
    print(f"Agua:{resources['water']}ml\nLeite:{resources['milk']}ml\nCafé:{resources['coffee']}g\nDinheiro:R${MONEY}")

def check_resources(choice):
    print(f"\nPreparando seu {choice}. Por favor esperar...")
    for i, necessario in MENU[choice]['ingredients'].items():
        if resources[i] < necessario:
            print(f"Desculpa, não temos {i} suficiente.")
            return False
    return True

def update_resources(bill, choice):
    global MONEY
    MONEY += bill
    for i, utilizado in MENU[choice]['ingredients'].items():
        resources[i] -= utilizado

def pagamento(choice):
    print("Por favor, realizar pagamento.\n")
    bill = MENU[choice]['cost']
    centavos = int(input("Quantas moedas de 50 centavos?:"))
    um_real = int(input("Quantas moedas de 1 Real?:"))
    dois_reais = int(input("Quantas notas de 2 Reais?:"))
    cinco_reais = int(input("Quantas notas de 5 Reais?:"))
    valor_input = (centavos * 0.5) + (um_real) + (dois_reais * 2) + (cinco_reais * 5)
    return check_pagamento(bill, valor_input, choice)

def check_pagamento(bill, valor_input, choice):
    troco = valor_input - bill
    if valor_input >= bill:
        print(f"Aqui o seu troco de {troco}R$")
        update_resources(bill, choice)
        return True
    else:
        print(f"Valor inserido insuficente,faltam {troco} R$ dinheiro restornado")
        return False

def main():
    while True:
        choice = input("\nO que você deseja ?(espresso/latte/cappuccino):")
        if choice == "off":
            break
        elif choice == "report":
            print_resources()
        elif choice in MENU:
            if check_resources(choice):
                pago = pagamento(choice)
                if pago:
                    print(f"Aqui está seu {choice}.Obrigado e volte sempre!")
            else:
                print("Transação não concluida")
        else:
            print("Opção invalida,digite novamente")

main()
