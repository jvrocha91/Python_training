from car_control import Car

def main():
    meu_carro = Car("Toyota", "Ethios",2019, "Prata")
    while True:
        option=input("'d' para acelerar, 'a' parar freiar, 'w' para exebir informações do veiculo, 's' para desligar o carro:")
        if option =='s':
            break
        elif option =='w':
            meu_carro.exibir_info_carro()
        elif option =='d':
            meu_carro.acelerar()
        elif option =='a':
            meu_carro.freiar() 

main()
        


