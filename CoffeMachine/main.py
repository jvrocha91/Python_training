MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

POWER = True
MONEY = 0

def print_resources():
    print(f"Agua:{resources['water']}ml\nLeite:{resources['milk']}ml\nCafé:{resources['coffee']}g\nDinheiro:R${MONEY}")

def check_resources(choice):
    print(f"Making your {choice}. Please wait...")
    for i , necessario in MENU[choice]['ingredients'].items():
        if resources[i] < necessario:
            print("Desculpa, não temos {i} o suficiente")
            return False
    return True

def pagamento(choice):
    print("Por favor, realizar pagamento.\n")
    bill=MENU[choice]['cost']
    centavos=int(input("Quantas moedas de 50 centavos?:"))
    um_real = int(input("Quantas moedas de 1 Real?:"))
    dois_reais = int(input("Quantas notas de 2 Reais?:"))
    cinco_reais = int(input("Quantas notas de 5 Reais?:"))
    valor_input = (centavos*0.5)+(um_real)+(dois_reais*2)+(cinco_reais*5)
    return check_pagamento(bill,valor_input,choice)

def check_pagamento(bill,valor_input,choice):
    if valor_input >= bill:
        troco=valor_input-bill
        print(f"Aqui o seu troco de {troco}R$")
        update_resources(bill,choice)
        return True
    else:
        print("Valor inserido insuficente, dinheiro restornado")
        return False

def update_resources(bill,choice):
    global MONEY
    MONEY += bill
    global resources
    for i in MENU[choice]['ingredients'].items():
        resources[i]-=

def start_menu():
    choice = input("O que você deseja ?(espresso/latte/cappuccino)")
    if choice == "off":
        global POWER
        POWER = False
    elif choice == "report":
        print_resources()
    elif choice in MENU:
        if check_resources(choice):
            pagamento(choice)
        else:
            print("Transação não concluida")

def main():
    while POWER:
        start_menu()

main()