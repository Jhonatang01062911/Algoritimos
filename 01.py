
#definição da função
def soma(numero):
    soma = sum(numero)
    print(f'\nA soma é {soma}')

def media(valores):
    avg = sum(valores) / len(valores) 
    print(f'A média é {avg}')

#criação da lista
lista = []

for a in range(5):
    lista.append(int(input('Digite um número: ')))

soma(lista)
media(lista)