peso = float(input('Digite o peso dos peixes: '))
multa = 4

if peso > 50:
    print(f'Há excesso de peso! {peso:.1f}kg')
    print(f'Você foi multado em: R${(peso - 50) * multa:.2f}')
elif peso <= 50:
    print('Você ainda está de acordo com o regulamento!')
