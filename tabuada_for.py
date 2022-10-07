tabuada = int((input("Digite um número para calcular sua tabuada: ")))
print("_ Tabuada de ", tabuada, "_")
for numero in range(1,11,1):
    # numeros entre 1 e 11, com incremento de 1 em 1
    # 11 não é incluído no 'range' e o laço será interrompido quando atingir esse valor
    print(str(tabuada), " x ", str(numero), " = ", str((tabuada * numero)))
    
