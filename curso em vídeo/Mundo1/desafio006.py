numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

# outro modo de calcular raiz quadrada: pow(numero,(1/2))

print('O dobro de {} é {}.'.format(numero, dobro))
print('O triplo de {} é {}.'.format(numero, triplo))
print('A raiz quadrada de {} é {:.2f}.'.format(numero, raiz_quadrada))

