# ESCREVE UM PROGRAMA QUE LEIA UM VALOR EM METROS
# E EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

valor_em_metros = int(input('Digite um valor: '))
convertcm = valor_em_metros * 10 * 10 
convertmm = valor_em_metros * 10 * 10 * 10 
print(f'o área tem {valor_em_metros} metros e o valor convertido para cm é {convertcm}cm e mm é {convertmm}mm')