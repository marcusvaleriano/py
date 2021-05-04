produto = float(input('Digite o valor do produto: '))
porcentagem = float(input('Digite o percentual de desconto: '))
desconto = produto * porcentagem / 100
print(f'O desconto foi de: {desconto}')
print(f'O valor do produto agora é de: {produto - desconto}')
