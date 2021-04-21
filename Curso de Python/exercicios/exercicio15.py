# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

vrum = float(input('digite quantos km percorrido: '))
dia = float(input('digite por quantos dias ele foi alugado: '))
valor_total = (vrum * 0.15) + (dia * 60)
print(f'o total a pagar é: {valor_total}')
