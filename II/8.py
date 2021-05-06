ganhoPorHora = float(input('Digite seu ganho por hora: '))
horasTrabalhadas = int(input('Digite a quantidade de horas trabalhas: '))

salarioBruto = ganhoPorHora * horasTrabalhadas

ir = salarioBruto * 11 / 100
inss = salarioBruto * 8 / 100
sindicato = salarioBruto * 5 / 100

salarioLiquido = salarioBruto - ir - inss - sindicato

print(f'- Seu salário bruto é: {salarioBruto:.2f}')
print(f'- IR: R${ir:.2}')
print(f'- INSS: R${inss:.2f}')
print(f'- Sindicato: R${sindicato:.2f}')
print(f'- Seu salário líquido é de: R${salarioLiquido:.2f}')
