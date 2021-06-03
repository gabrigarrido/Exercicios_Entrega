"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e ímpares em ordem crescente"""

todos = list()
pares = list()
impares = list()

for x in range (0, 7):
  numeros = int(input('Digite um número: '))
  todos.append(numeros)
  if numeros % 2 == 0:
    pares.append(numeros)
  else:
    impares.append(numeros)
  pares.sort()
  impares.sort()


print('----'*25)
print(f'Aqui está os números que você digitou: {todos} \n')
print(f'Os números pares são: {pares} \n')
print(f'Os números impares são: {impares} \n')
