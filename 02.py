#Utilizando estruturas de repetição com variavel de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input("Por Favor, informe uma frase: \n ")
vogais = 0

for x in frase:
  if x in 'aeiou':
    vogais += 1

print(f"A frase possui {vogais} vogais \n")

for i in 'aeiou':
  frase = frase.replace(i, '')

print(f"A sua frase sem as vogais seria assim: \n {frase}")