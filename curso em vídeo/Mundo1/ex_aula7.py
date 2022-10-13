valor = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

soma = valor + valor2
multiplicacao = valor * valor2
divisao = valor / valor2
divisao_inteira = valor // valor2
potencia = valor ** valor2

print('A soma é igual a {},\no produto vale {} \ne a divisão é {}.'.format(soma, multiplicacao, divisao), end=' ')
print('\nE ainda a divisão inteira é igual a {} \ne a potência é {}.'.format(divisao_inteira, potencia))
