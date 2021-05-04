cigarros = int(input('Digite a quantidade de cigarros por dia: '))
anosFumando = int(input('Digite a quantidade de anos fumando: '))
totalCigarros = anosFumando * 365 * cigarros
dias = totalCigarros / 1440
print(f'Fodeu você perdeu {dias:.1f} dias de vida')
