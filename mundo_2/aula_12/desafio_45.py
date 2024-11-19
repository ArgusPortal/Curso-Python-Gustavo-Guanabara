from random import choice
from time import sleep

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

# Lista com as opções de jogadas possíveis
lista = ["pedra", "papel", "tesoura"]

# Exibe as regras do jogo para o usuário
print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

# Solicita ao usuário que escolha entre pedra, papel ou tesoura e converte a entrada para minúsculas
jogador = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

# Exibe a contagem regressiva para o jogo
print("JO")
sleep(0.50)  # Pausa de 0.5 segundos
print("KEN")
sleep(0.5)   # Pausa de 0.5 segundos
print("PÔ!!! \n")

# Escolhe aleatoriamente uma jogada para o computador
computador = choice(lista)

# Exibe a escolha do computador
print(f"Computador escolheu: {computador}\n")

# Verifica o resultado do jogo
if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
else:
    print("Computador venceu!")
