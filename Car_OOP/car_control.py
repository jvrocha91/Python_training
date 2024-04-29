class Car():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
        self.velocidade+=10
        print(f"Velocidade:{self.velocidade}")
    
    def freiar(self):
        if self.velocidade > 0:
            self.velocidade-=10
            print(f"Velocidade:{self.velocidade}")
        else:
            print(f"O carro está parado. Velocidade:{self.velocidade}")

    def exibir_info_carro(self):
        print(f"\n===Informações do carro==\nMarca:{self.marca}\nModelo:{self.modelo}\nAno:{self.ano}\nCor:{self.cor}\n")
        
