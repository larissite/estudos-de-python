largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura

total_tinta = area / 2

print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m².\nPara pintar toda a parede'
      'será necessário {}l de tinta.'.format(largura, altura, area, total_tinta))

