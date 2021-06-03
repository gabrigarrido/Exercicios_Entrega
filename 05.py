#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras que foram retiradas da frase original.

frase = input("Por Favor, informe uma frase: \n ")

def contar_vogais(frase):
  vogais = 0
  for x in frase:
    if x in 'aeiou':
      vogais += 1

  print(f"A frase possui {vogais} vogais \n")
#incompleto
