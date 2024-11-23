# Uma fábrica tem 10 representantes. Cada um recebe uma comissão calculada a partir
# do número de itens de um pedido, segundo os seguintes critérios:
#
#     – para até 19 itens vendidos, a comissão é de 10% do valor total do pedido;
#     – para pedidos de 20 a 49 itens, a comissão é de 15% do valor total do pedido;
#     – para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do pedido; e
#     – para pedidos iguais ou superiores, a 75 itens a comissão é de 25%.
#
# Faça um programa que lê a quantidade de itens de pedidos de cada representante e
# imprime o percentual de comissão de cada um.


for representante in range(10):
    comissao = "0%"
    print(f"Representante número {representante + 1}.")
    vendas = int(input("Digite o número de itens vendidos: "))

    if vendas < 0:
        print("Não é possível calcular a comissão, valor digitado é inválido.")
    elif vendas < 20:
        comissao = "10%"
    elif vendas >= 20 and vendas < 50:
        comissao = "15%"
    elif vendas >= 50 and vendas < 75:
        comissao = "20%"
    elif vendas >= 75:
        comissao = "25%"

    print(f"A comissão do representante {representante + 1} é de {comissao}.")
    print("-" * 70, "\n")

print("=" * 70)

# Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 15 pessoas.
# Faça um programa que calcule e mostre:
#
#     – a maior e a menor altura do grupo
#     – a média de altura das mulheres
#     – o número de homens
#     – o sexo da pessoa mais alta

sexo_maior_altura = ""
sexo_menor_altura = ""
maior_altura = -1
menor_altura = 10000
media_altura_Fem = 0
total_Masc = 0

for pessoa in range(15):
    print(f"Coleta {pessoa + 1}/15")
    sexo = input("Digite qual é o seu sexo, (M)asculino/(F)eminino: ")
    altura = float(input("Digite a sua altura (m): "))

    if sexo in "MF":
        if altura > maior_altura:
            maior_altura = altura
            sexo_maior_altura = sexo

        if altura < menor_altura:
            menor_altura = altura
            sexo_menor_altura = sexo

        if sexo == "M":
            total_Masc += 1

        elif sexo == "F":
            media_altura_Fem += altura
            if pessoa == 15:
                media_altura_Fem /= 15

    else:
        print("O sexo digitado é inválido, os dados não serão computados")
    
    print("-" * 70, "\n")

print(
    f"A maior altura é de {maior_altura} e é uma pessoa do sexo {sexo_maior_altura}\n",
    f"A menor altura é de {menor_altura} e é uma pessoa do sexo {sexo_menor_altura}\n",
    f"O total de pessoas do sexo Masculino é: {total_Masc}\n",
    f"A média da altura feminina é de: {media_altura_Fem:.2f}\n",
)

print("=" * 70)

# Em uma eleição presidencial com 15 eleitores existem 3 candidatos. Os votos são
# informados por meio de código. Os códigos utilizados são:
#     – 1 – Candidato A,
#     - 2 - Candidato B,
#     - 3 – Candidato C,
#     - 4 - Voto Nulo e
#     - 5 - Voto em Branco
#
# Faça um programa que leia os votos de cada eleitor, calcule e mostre:
#     – O total de votos para cada candidato
#     – O total de votos nulos
#     – O total de votos em branco
#     – A percentagem de votos nulos sobre o total de votos;
#     – A percentagem de votos em branco sobre o total de votos.

total_votos_A = 0
total_votos_B = 0
total_votos_C = 0
total_votos_nulos = 0
total_votos_brancos = 0
porcentagem_nulos = 0
porcentagem_brancos = 0

for voto in range(15):
    print(
        "Qual será o seu voto?\n\n",
        "(1) - Candidato A\n",
        "(2) - Candidato B\n",
        "(3) - Candidado C\n",
        "(4) - Voto nulo\n",
        "(5) - Voto em branco\n", 
        "*Valores inválidos serão contabilizados como nulo.\n\n"
        f"Digite sua escolha ({voto + 1}/15): ", end="",
    )
    escolha = input()

    print("-" * 70, "\n")

    if escolha == '1':
        total_votos_A += 1
    elif escolha == '2':
        total_votos_B += 1
    elif escolha == '3':
        total_votos_C += 1
    elif escolha == '4':
        total_votos_nulos += 1
    elif escolha == '5':
        total_votos_brancos += 1
    else:
        total_votos_nulos += 1

    porcentagem_nulos = (total_votos_nulos / 15) * 100
    porcentagem_brancos = (total_votos_brancos / 15) * 100

print(
    f"Estatísticas da eleição:\n\n\t",
    f"Votos para o canditado A: {total_votos_A}\n\t",
    f"Votos para o candidato B: {total_votos_B}\n\t",
    f"Votos para o canditado C: {total_votos_C}\n\t",
    f"Votos nulos: {total_votos_nulos}\n\t",
    f"Votos em branco: {total_votos_brancos}\n\t",
    f"Porcentagem de votos nulos: {porcentagem_nulos:.2f}%\n\t"
    f"Porcentagem de votos em branco: {porcentagem_brancos:.2f}%\n"
)

print("=" * 70, '\n')

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade 
# de números pares e a quantidade de números impares.

contador_par = 0
contador_impar = 0

for i in range(10):
    numero = int(input(f"Digite um número ({i + 1}/10): "))
    if numero % 2 == 0:
        contador_par += 1
    elif numero % 2 == 1:
        contador_impar += 1

print(f"A quantidade de números pares foi {contador_par} e impares {contador_impar}.")
print("=" * 70, '\n')

# O Departamento Estadual de Meteorologia te contratou para desenvolver um programa 
# que leia um conjunto de 100 temperaturas, e informe ao final a menor e a maior 
# temperaturas informadas, bem como a média das temperaturas.

menor_temperatura = 100000
maior_temperatura = -1
soma_temperaturas = 0

for i in range(100):
    temperatura = int(input(f"Digite a temperatura {i + 1}/100: "))
    soma_temperaturas += temperatura

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

media_tempeatura = soma_temperaturas / 100
print(
    f"Maior temperatura: {maior_temperatura} C\n",
    f"Menor temperatura: {menor_temperatura} C\n",
    f"Média das temperatura: {media_tempeatura} C"
)
print("=" * 70, '\n')
