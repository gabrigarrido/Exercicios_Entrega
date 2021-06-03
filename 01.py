#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
   

while True:
  try: 
    numero01 = int(input("Por favor informe o primeiro número: \n"))
    numero02 = int(input("Por favor digite o segundo número: \n"))
    break
  except ValueError:
    print("É necessário ser um número inteiro!!")

def soma_numeros(numero01, numero02):
  soma = numero01+numero02
  print(f"A soma dos numeros é {soma}")

def multiplica_numeros(numero01, numero02):
  multiplica = numero01*numero02
  print(f"A multiplicação dos numeros é {multiplica}")

def divisao_inteira(numero01, numero02):
  divisao = numero01 // numero02
  print(f"A divisao inteira entre os dois numeros é {divisao}")
  return divisao_inteira

def maior_numero(numero01, numero02):
  if numero01 > numero02:
    print(f"O maior numero é o {numero01}")
  elif numero01 == numero02:
    print("Os números são iguais")
  else:
    print(f"O maior numero é o {numero02}")

def par_impar(numero01, numero02):
  soma = numero01 + numero02
  if soma % 2 == 0:
    print("O numero é par")
  else:
    print("O numero é impar")

def resto_divisao(numero01, numero02):
  if (numero01*numero02) > 40:
    operacao = (numero01*numero02) // (numero01//numero02)
    print(f"O resultado da soma dividido pela divisao inteira é {operacao}")
  else:
    print("A multiplicacao entre os dois numeros não foi maior que 40!")

print('--'*25)
soma_numeros(numero01, numero02)
multiplica_numeros(numero01, numero02)
divisao_inteira(numero01, numero02)
maior_numero(numero01, numero02)
par_impar(numero01, numero02)
resto_divisao(numero01, numero02)
     

    
