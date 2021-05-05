l1 = int(input('Insira o primeiro lado do triângulo: '))
l2 = int(input('Insira o segundo lado do triângulo: '))
l3 = int(input('Insira o terceiro lado do triângulo: '))

if l1 == l2 and l1 == l3:
    print('É um triângulo equilátero!')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um triângulo isósceles!')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('É um triângulo escaleno')
