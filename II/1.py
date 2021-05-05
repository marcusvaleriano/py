velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 110:
    print(f'Você foi multado no valor de: R${(velocidade - 110) * 5}')
else:
    print('Você não foi multado')
