# o vídeo sugere a tabuada com prints linha a linha, conforme exemplo abaixo:
# tabuada = int((input("Digite um número para calcular sua tabuada: ")))
# print('{} x {} = {}'.format(tabuada, 1, tabuada*1))

# como eu já havia feito tabuada com laço de repetição 'for', reproduzo abaixo com algumas alterações:
tabuada = int((input('Digite um número para calcular sua tabuada: ')))
print('_ Tabuada de {} _'.format(tabuada))
for numero in range(1, 11, 1):
    # numeros entre 1 e 11, com incremento de 1 em 1
    # 11 não é incluído no 'range' e o laço será interrompido quando atingir esse valor
    print('{:2} x {:2} = {:2}'.format(tabuada, numero, (tabuada * numero)))

