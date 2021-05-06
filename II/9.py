metrosQuadrados = int(input('Digite o tamanho em metros quadrados: '))

litros = 18 * 3
preco = 80

if metrosQuadrados % litros == 0:
    latas = metrosQuadrados / litros
else:
    latas = int(metrosQuadrados / litros) + 1

valorFinal = latas * preco

print(f'A quantidade de latas é: {latas}')
print(f'O preço final foi de: R${valorFinal:.2f}')
