# Ler um número inteiro e exibir seu dobro
numero = int(input("Digite um número inteiro: "))
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}")

# Exibir a multiplicação de dois números reais informados pelo usuário.
real1 = float(input("Digite um número Real: "))
real2 = float(input("Digite o segundo número Real: "))
multi = real1 * real2
print(f"A multiplicação de {real1} por {real2} é igual a {multi:.2f}")

# Calcular a média aritmética de três notas fornecidas pelo usuário.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A sua média é de: {media:.2f}")

# A imobiliária XYZ vende apenas terrenos retangulares. 
# Faça um programa para ler as dimensões de um terreno e exibir a área do mesmo.
largura = float(input("Qual é a largura do terreno em metros? "))
comprimento = float(input("Qual o comprimento do terro em metros?"))
area_total = largura * comprimento
print(f"Temos um terro de {largura:.2f} de largura e {comprimento:.2f} ", end='')
print(f"de comprimento, totalizando {area_total:.2f} m²")

# Faça um programa para ler o salário de um funcionário e aumentá-lo em 20%.
# Imprima seu salário final.
salario = float(input("De quanto é o seu salário? "))
aumento = salario * .2
novo_salario = salario + aumento
print(f"Um salário de R${salario:.2f} como um aumento de 20% fica R${novo_salario:.2f}")

# Ler o valor de um cheque e escrever o quanto vai ser recolhido de CPMF.
# Considere que imposto recolhe uma taxa de 0,3%. Imprimir o valor do imposto.
cheque = float(input("Digite o valor do cheque: "))
imposto = cheque * .003
cheque_descontado = cheque - imposto
print(f"O seus cheque de R${cheque:.2f} após a taxa de R${imposto:.2f}", end='')
print(f" resulta em um saldo de R${cheque_descontado:.2f}")

# Escreva uma seqüência de comandos para solicitar o nome e a matrícula do aluno.
# Em seguida exibir as informações no seguinte formato:
# – Nome do Aluno: “XXXXXXXX”, Matrícula: “ZZZZ”
nome = input("Digite seu nome completo: ")
matricula = input("Digite sua matrícula: ")
print(f"Nome do aluno: {nome}, matrícula: {matricula}")
