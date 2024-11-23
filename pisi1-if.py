# Ler um número inteiro e dizer se é par ou ímpar.
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"{numero} é par.")
elif numero % 2 == 1:
    print(f"{numero} é ímpar.")

print("=" * 70)
# Ler a temperatura de uma pessoa e exibir a mensagem “Febre Alta” (temp ≥ 39),
# “Febril” (39 > temp ≥ 37) ou “Sem Febre” (temp < 37).
temperatura = float(input("Digite sua temperatura: "))
if temperatura >= 39:
    print("Febre Alta.")
elif temperatura < 37:
    print("Sem Febre.")
else:
    print("Febril")

print("=" * 70)
# Entrar com um distância (km) e o tempo de viagem (horas) de um automóvel,
# e dizer se a velocidade média foi superior ao limite (110 km/h) ou não.
distacia = float(input("Digite a distância (km): "))
tempo = float(input("Digite o tempo da viagem (horas): "))
kmh = distacia / tempo
if kmh > 110:
    print("Você passou do limite de velocidade.")
else:
    print("Você está dentro do limite de velocidade.")

print("=" * 70)
# Faça um Programa que peça para entrar com um ano (inteiro com 4 dígitos) e
# determine se o mesmo é ou não bissexto (divisível por 4).
ano = int(input("Digite um ano: "))
if ((ano % 4 == 0) and (ano % 100 != 0)) or ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não'e bissexto.")

print("=" * 70)
# Faça um Programa que leia três números e mostre-os em ordem decrescente.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 >= numero2) and (numero1 >= numero3) and (numero2 >= numero3):
    print(f"Ordem decrescente: {numero1}, {numero2} e {numero3}")
elif (numero1 >= numero2) and (numero1 >= numero3) and (numero3 >= numero2):
    print(f"Ordem decrescente: {numero1}, {numero3} e {numero2}")
elif (numero2 >= numero1) and (numero2 >= numero3) and (numero1 >= numero3):
    print(f"Ordem decrescente: {numero2}, {numero1} e {numero3}")
elif (numero2 >= numero1) and (numero2 >= numero3) and (numero3 >= numero1):
    print(f"Ordem decrescente: {numero2}, {numero3} e {numero1}")
elif (numero3 >= numero1) and (numero3 >= numero2) and (numero2 >= numero1):
    print(f"Ordem decrescente: {numero3}, {numero2} e {numero1}")
elif (numero3 >= numero1) and (numero3 >= numero2) and (numero1 >= numero2):
    print(f"Ordem decrescente: {numero3}, {numero2}, {numero1}")
else:
    print("Algum dos valores é imválido.")

print("=" * 70)
# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input("Preço do primeiro produto (R$): "))
produto2 = float(input("Preço do segundo produto (R$): "))
produto3 = float(input("Preço do terceiro produto (R$): "))

if (produto1 <= produto2) and (produto1 <= produto3):
    print(f"O menor produto tem o preço de R${produto1:.2f}")
elif (produto2 <= produto1) and (produto2 <= produto3):
    print(f"O menor produto tem o preço de R${produto2:.2f}")
elif (produto3 <= produto1) and (produto3 <= produto2):
    print(f"O menor produto tem o preço de R${produto3:.2f}")

print("=" * 70)
# Faça um Programa que pergunte em que turno a pessoa estuda. Peça para digitar
# M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print(
    "Digite qual é o turno que você estuda:\n\t",
    "(M) - Matutino;\n\t" "(V) - Vespertino;\n\t" "(N) - Noturno.\n",
    "input: ",
    end="",
)
turno = input()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("O valor digitado é inválido.")

print("=" * 70)
# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
# inválido.

dia_semana = input("Digite o dia da semana (1 - 7): ")

if dia_semana == "1":
    print(f"{dia_semana} corresponde ao Domingo.")
elif dia_semana == "2":
    print(f"{dia_semana} corresponde a Segunda-Feira.")
elif dia_semana == "3":
    print(f"{dia_semana} corresponde a Terça-Feira.")
elif dia_semana == "4":
    print(f"{dia_semana} corresponde a Quarta-Feira.")
elif dia_semana == "5":
    print(f"{dia_semana} corresponde a Quinta-Feira.")
elif dia_semana == "6":
    print(f"{dia_semana} corresponde a Sexta-Feira.")
elif dia_semana == "7":
    print(f"{dia_semana} corresponde ao Sábado.")
else:
    print("O valor digitado é inválido.")

print("=" * 70)
