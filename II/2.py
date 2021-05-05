minutos = int(input('Digite a quantidade de minutos: '))
cobranca = 0

if minutos < 200:
    cobranca = 0.20
    print(f'Sua conta telefonica é de: R${minutos * 0.20:.2f}')

elif minutos <= 400:
    cobranca = 0.18
    print(f'Sua conta telefonica é de: R${minutos * 0.18:.2f}')

elif minutos > 400:
    cobranca = 0.15
    print(f'Sua conta telefonica é de: R${minutos * 0.15:.2f}')

elif minutos > 800:
    cobranca = 0.08
    print(f'Sua conta telefonica é de: R#{minutos * 0.08:.2f}')
