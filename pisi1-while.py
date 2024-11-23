# Crie um programa que lê as idades e alturas de alguns alunos. A condiçãode 
# parada é a altura = 0. Em seguida, o programa deve informar quantos alunos com 
# mais de 13 anos possuem altura inferior à 1.5.

altura = -1
contador = 0

while altura != 0:
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura em metros (digite 0 para sair): "))
    
    if idade > 13 and altura > 1.5:
        contador += 1

print(f"O número de alunos maiores de 13 anos e maiores que 1.5m é: {contador}")
print('=' * 70)

# Escreva um programa que lê uma quantidade indeterminada de números inteiros e 
# escreve todos os que forem ímpares positivos (use o ‘continue’. Considerar o 
# valor 99 como fim da entrada.

numero = -1
string = ''

while numero != 99:
    numero = int(input("Digite um número (digite 99 para sair): "))

    if numero == 99:
        continue

    if (numero > 0) and (numero % 2 == 1):
        string = string + str(numero) + " "

print(f"Lista de números ímpares positivos: {string}")
print('=' * 70)

# Faça um programa que imprima o fatorial de um número. O valor de entrada deve 
# ser menor ou igual a 20.

numero = int(input("Dite um número para ser mostrado seu fatorial (menor que 20): "))
multiplicador = numero
fatorial = 1

if numero > 20 or numero < 0:
    print("O fatorial não será computado, você digitou um número maior que 20 ou menor que 0.")

while multiplicador > 1 and multiplicador > 0:
    fatorial *= multiplicador
    multiplicador -= 1

print(f"O fatorial de {numero} é: {fatorial}")
print('=' * 70)

# Faça um programa que identifica os 15 primeiros números primos (utilizando a
# instrução break).

primos_str = ''
total_primos = 0
numero = 2

while True:
    contador = 0
    divisor = 1

    if total_primos >= 15:
        break

    while divisor <= numero:
        if numero % divisor == 0:
            contador += 1
        divisor += 1

    if contador == 2:
        primos_str = primos_str + str(numero) + ' '
        total_primos += 1

    numero += 1

print(f"Os primeiros 15 númeors primos são: {primos_str}")
print('=' * 70)

# Faça um algoritmo que peça dois números – base e expoente – calcule e mostre o 
# primeiro número elevado ao segundo número. Não utilize a função de potência da 
# linguagem.

base = int(input("Digite qual é a base: "))
expoente = int(input("Digite qual é o exponte: "))
repeticao_base = 1
repeticao_expoente = 1
valor_total = 1

while repeticao_expoente <= expoente:
    valor_total *= base
    repeticao_expoente += 1

print(f"O resultado é: {valor_total}")
print('=' * 70)

# Faça um programa que peça 5 valores positivos do usuário (usando while). Caso o 
# usuário digite algum número negativo o programa deve terminar imediatamente. 
# Caso termine normalmente informe que os dados foram inseridos com sucesso (use o else).

numero = 0
contador = 0

while contador <= 5:
    numero = float(input("Digite um número (número negativo para sair): "))
    if numero < 0:
        break
    contador += 1

else:
    print("Os dados foram inseridos com sucesso.")
print('=' * 70)

# Faça o algoritmo de imprimir a tabuada de um número fornecido pelo usuário,
# usando while. Após mostrar a tabuada o programa deve perguntar se deseja imprimir 
# a tabuada de um novo número.

numero = 0
resposta = ''

while resposta != 'N':
    numero = int(input("Digite um número para mostrar sua tabuáda: "))
    tabuada = 1
    while tabuada <= 10:
        multi = numero * tabuada
        print(f"{numero} x {tabuada} = {multi}")
        tabuada += 1
    resposta = input("Deseja continuar? (N)ão para sair.")
