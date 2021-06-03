#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

lista_meses = ["janeiro", "fevereiro","março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novemvbro", "dezembro"]


def mes_por_extenso():
  data = input("Digite a data no formato DD/MM/AAAA e devolva uma string no formado DD de mesPorExtenso: \n")
  print(
  (data.split('/')[0] +
  " de " + lista_meses[(int(data.split("/")[1])-1)] + " de " + data.split("/")[2]))

mes_por_extenso()


