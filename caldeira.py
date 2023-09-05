import math
import random

def simulacaocaldeiraam53(t, tempoMax, volumeAgua0, temperatura_inicial):
    
    VolumeAgua = max(volumeAgua0 * (1 - (t / tempoMax) / (1 + 0.01 * math.cos(t))) - 1 * random.uniform(1, 10), 20)
    pressao = min((volumeAgua0 / VolumeAgua) + 1 * (volumeAgua0 / (1 + math.exp(-0.09 * (t - tempoMax / 2))) + math.sin(2 * t / tempoMax)) - 1 * random.uniform(1, 10), 80)
    temperatura = min(temperatura_inicial / pressao + 20 * t / tempoMax * 10 * math.cos(t / tempoMax) - 1 * random.uniform(1, 10), 90)
    
    V = [t, VolumeAgua, pressao, temperatura]
    return V

print("====SISTEMA DE SIMULÇÃO DE CALDEIRA====\nCONTROLE DE TEMPERATURA, PRESSÃO E VOLUME DE ÁGUA DA CALDEIRA\n")

while True:
    tempoMax = int(input("\nQual o tempo maximo da simulação(Minutos):"))
    t = int(input("\nQual o tempo da simulação atual(Minutos):"))

    if t > tempoMax:
        print("\nTempo de simulação inválido, digite novamente um valor menor que o tempo máximo")
        continue

    volumeAgua0 = int(input("\nDigite o volume inicial de água na caldeira (Litros),deve estar entre 20 e 50 litros:"))
    if volumeAgua0 < 20 or volumeAgua0 > 50:
        print("\nValor inválido, inicie simulação novamente.")
        continue

    temperatura_inicial = int(input("\nDigite a temperatura inicial da água (não pode ser maior que 90):"))
    if temperatura_inicial > 90:
        print("\nTemperatura inválida, inicie simulação novamente.")
        continue

    V = simulacaocaldeiraam53(t, tempoMax, volumeAgua0, temperatura_inicial)

    print(f"\n====RESULTADO DA SIMULAÇÃO====\n\n1-Tempo da simulação:{V[0]} minutos\n\n2-Volume de água:{V[1]}\n\n3-Pressão da água:{V[2]}\n\n4-Temperatura:{V[3]}")

    op = input("Deseja continuar? (s/n)")
    if op.lower() != 's':
        break
 
 
 
