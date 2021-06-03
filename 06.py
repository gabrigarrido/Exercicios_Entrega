#06 - Utilizando perguntass faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 'Telefonou para a vítima?'
# 'Esteve no local do crime?'
# 'Mora perto da vítima?'
# 'Devia para a vítima?'
# 'Já trabalhou com a vítima?'
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#Entre 3 e 4 como "Cúmplice" e 5 como "Assassino"
#Caso contrário, ele será classificado como "Inocente".

soma = 0

pergunta01 = input("Telefonou para a vitima? [S/N]")
pergunta02 = input("Esteve no local do crime? [S/N]")
pergunta03 = input("Mora perto da vitima? [S/N]")
pergunta04 = input("Devia para a vitima? [S/N]")
pergunta05 = input("Já trabalhou com a vítima? [S/N]")

perguntas = [pergunta01, pergunta02, pergunta03, pergunta04, pergunta05]
print(perguntas)

for i in perguntas:
    if i == "s" or "S":
        soma += 1

if (soma < 2):
  print("Inocente")
elif (soma == 2):
  print("Suspeita")
elif (3 <= soma <= 4):
  print("Cumplice")
elif (soma == 5):
  print("Assassino")