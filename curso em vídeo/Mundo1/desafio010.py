real = float(input('Quantos reais você tem na carteira? R$: '))
dolar = real / 5.28 #cotação do dólar em 19/10/22
euro = real / 5.17 #cotação do euro em 19/10/22

print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}!'.format(real, dolar, euro))
