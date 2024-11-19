''' 
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

# Solicita ao usuário um número inteiro para ser convertido e converte para int
num = int(input("Digite um número a ser convertido: \n"))

# Solicita ao usuário que escolha a base de conversão e converte para int
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3

Sua escolha: \n'''))

# Verifica se a base escolhida é 1 (binário)
if base == 1:
    print("Você escolheu binário.")
    # Converte o número para binário e remove o prefixo '0b'
    print("{} convertido para binário é: {}.".format(num, bin(num)[2:]))
# Verifica se a base escolhida é 2 (octal)
elif base == 2:
    print("Você escolheu octal.")
    # Converte o número para octal e remove o prefixo '0o'
    print("{} convertido para octal é: {}.".format(num, oct(num)[2:]))
# Verifica se a base escolhida é 3 (hexadecimal)
elif base == 3:
    print("Você escolheu hexadecimal.")
    # Converte o número para hexadecimal e remove o prefixo '0x'
    print("{} convertido para hexadecimal é: {}.".format(num, hex(num)[2:]))
else:
    print("Por favor, escolha apenas uma das 3 opções.")
