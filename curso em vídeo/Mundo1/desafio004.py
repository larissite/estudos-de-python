qual_tipo = input('Digite algo: ')
print('O tipo primitivo do valor digitado é', type(qual_tipo))
print('É um número?', qual_tipo.isnumeric())
print('É alfabético?', qual_tipo.isalpha())
print('É alfanumérico?', qual_tipo.isalnum())
print('Está em maiúsculas?', qual_tipo.isupper())
print('Está em minúsculas?', qual_tipo.islower())
print('Está capitalizada?', qual_tipo.istitle())
