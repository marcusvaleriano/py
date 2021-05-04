salario = float(input('Digite seu salário: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))
aumento = salario * porcentagem / 100
print(f'O aumento foi de: R${aumento}')
print(f'O salário total ficou em: R${salario + aumento}')
