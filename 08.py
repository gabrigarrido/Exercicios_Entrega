#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 para se aposentar.


pessoa = {
  
}

pessoa['nome'] = input("Por favor digite seu nome: ")
nascimento = int(input("Por favor, digite seu ano de nascimento no formato AAAA: \n"))
pessoa['idade'] = (2021 - nascimento)
#print(nascimento)
#pessoa['idade']
pessoa['ctps'] = int(input("Digite os números da sua Carteira de Trabalho: \n"))

if pessoa['ctps'] != 0:
  pessoa['ano'] = int(input("Informe o ano de contratação do seu trabalho: \n"))
  pessoa['salario'] = int(input("Informe o último salário ganho: \n"))
  pessoa['aposentadoria'] = ((pessoa['ano']+ 35) - nascimento)

print('---'*25)

if pessoa['ctps'] !=0:
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos, foi contratado em {pessoa['ano']} com um salário de {pessoa['salario']} reais e ira se aposentar com {pessoa['aposentadoria']} anos.")
else:
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos e não possui carteira de trabalho no momento.")


