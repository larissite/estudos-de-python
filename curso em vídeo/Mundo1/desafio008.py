distancia = float((input('Digite uma distância em metros: ')))

distancia_milimetros = distancia * 1000
distancia_centimetros = distancia * 100
distancia_decimetros = distancia * 10
distancia_decametros = distancia / 10
distancia_hectometros = distancia / 100
distancia_km = distancia / 1000

print('A distancia {} em metros equivale a {} milímetros, {} centimetros, {} decímetros.'
      .format(distancia, distancia_milimetros, distancia_centimetros, distancia_decimetros))
print('Também equivale a {} decâmetros, {} hectômetros e {} quilômetros.'
      .format(distancia_decametros, distancia_hectometros, distancia_km))

