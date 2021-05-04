dias = int(input('Digite uma quantidade de dias: '))
horas = int(input('Digite uma quantidade de horas: '))
minutos = int(input('Digite uma quantidade de minutos: '))
segundos = int(input('Digite uma quantidade de segundos: '))
total = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
print(f'O total de segundos é: {total}')
