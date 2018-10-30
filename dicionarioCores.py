colors = {'vermelho': 'red', 'azul': 'blue', 'verde': 'green', 'preto': 'black'}

color = input('Digite uma cor que deseja traduzir: ').lower()

traducao = colors.get(color,'Esta cor não consta no meu dicionário')

print(traducao)
