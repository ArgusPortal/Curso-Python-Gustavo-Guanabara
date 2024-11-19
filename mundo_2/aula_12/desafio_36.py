'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

# Solicita o valor da casa ao usuário e converte para float
preco = float(input("Qual o valor da casa? \n"))

# Solicita o salário do comprador e converte para float
sal = float(input("Qual é o seu salário? \n"))

# Solicita em quantos anos o comprador vai pagar e converte para int
tempo = int(input("Em quantos anos você vai pagar? \n"))

# Calcula o valor da prestação mensal dividindo o preço da casa pelo número total de meses
mensalidade = (preco / (tempo * 12))

# Exibe o valor da casa formatado com duas casas decimais
print("Valor da casa: {:.2f}".format(preco))

# Exibe o valor da prestação mensal formatado com duas casas decimais
print("Prestação: {:.2f}".format(mensalidade))

# Verifica se a prestação mensal é maior ou igual a 30% do salário do comprador
if mensalidade >= (sal * 30 / 100):
    # Se a prestação for maior ou igual a 30% do salário, o empréstimo é negado
    print("Empréstimo negado.")
else:
    print('''Empréstimo concedido.
    Mensalidade durante {} anos: R${:.2f}.'''.format(tempo, mensalidade))
