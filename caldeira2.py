import matplotlib.pyplot as plt
import numpy as np
import math
import random

def simulacaocaldeiraam53(tempomax, volumeaguainicial):
    
    VolumeAgua = max(volumeaguainicial* (1 - (t / tempomax) / (1 + 0.01 * math.cos(t))) - 1 * random.uniform(1, 10), 20)
    pressao = min((volumeaguainicial / VolumeAgua) + 1 * (volumeaguainicial / (1 + math.exp(-0.09 * (t - tempomax / 2))) + math.sin(2 * t / tempomax)) - 1 * random.uniform(1, 10), 80)
    temperatura = min(temperatura / pressao + 20 * t / tempomax * 10 * math.cos(t / tempomax) - 1 * random.uniform(1, 10), 90)
    
    V = [t, VolumeAgua, pressao, temperatura]
    return V
  
def simulacaografico():
    while True:
        print("**************************************")
        print("***** SIMULAÇÃO DA CALDEIRA AM53 *****")
        print("**************************************")

        tempomax = int(input("DIGITAR O TEMPO MÁXIMO DE SIMULAÇÃO [MINUTOS]: "))
        volumeaguainicial = int(input("DIGITAR O VOLUME INICIAL DE ÁGUA [LITROS]: "))
        print("\n")
        
        r = simulacaocaldeiraam53(tempomax, volumeaguainicial)
        for i in r:
            print(i)

        plt.title("AZUL-Tempo VERDE-Pressão LARANJA-Volume Água VERMELHO-Temperatura")
        plt.plot(r)
        plt.show()
        print("\n")

        opcao = input("DESEJA REALIZAR OUTRA SIMULAÇÃO <S/N>: ")
        if opcao == "n" or opcao == "N":
            break
        
    print("\n\n***** OBRIGADO POR UTILIZAR O SIMULADOR DE CALDEIRA AM53 *****")

simulacaografico()

  
    



 
 
 