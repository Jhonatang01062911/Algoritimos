#Lado do Triângulo
l1  =  float(input('Tamanho do primeiro lado: '))
l2  =  float(input('Tamanho do segundo lado: '))
l3  =  float(input('Tamanho do terceiro: '))
#Saber se pode ou nao pode criar um Triângulo com Tamnhos dos Lados digitados
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmento PODEM FORMAR um triângulo : ', end='')
# Operação Para Saber se da para fazer um Triângulo EQUILÁTERO
    if l1 == l2 == l3:
        print('EQUILÁTERO .')
# Operação Para Saber se da para fazer um Triângulo ESCALENO
    elif l1 != l2 != l3 != l1:
        print('ESCALENO .')
# Operação Para Saber se da para fazer um Triângulo ISÓCELES
    else:
        print('ISÓCELES .')
else:
    print('Os segmento acima NÃO PODEM formar um triangulo')