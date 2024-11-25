# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu 
# comprimento. Informe também se as duas strings possuem o mesmo comprimento  e 
# são iguais ou diferentes no conteúdo.
print("Compare duas Strings.")
string1 = input("Primeira string: ")
string2 = input("Segunda string: ")

print(
    f"Tamanho de \"{string1}\": {len(string1)} caracteres.\n",
    f"Tamanho de \"{string2}\": {len(string2)} caracteres."
)

if len(string1) == len(string2):
    print("As duas strings são do mesmo tamanho.")
else:
    print("As duas strings são de tamanhos diferentes.")

if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdos diferentes.")

print("=" * 70, '\n')

# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre 
# o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas 
# ou minúsculas.

nome = input("Digite o seu nome: ")
print(f"{nome[::-1].upper()}")
print("=" * 70, '\n')

# Faça um programa que solicite o nome do usuário e imprima-o na vertical.

nome = input("Digite o seu nome: ")
for letra in nome:
    print(f"{letra.upper()}")
print("=" * 70, '\n')

# Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = input("Digite o seu nome: ")
escada = ''

for letra in nome:
    escada += letra
    print(f"{escada.upper()}")
print("=" * 70, '\n')

# Faça um programa que lê uma string e conta quantas vezes o substring “ado” 
# aparece na string.

string = input("Escreva uma frase: ")
count_ado = string.count("ado")
print(f"A substring 'ado' aparece {count_ado} vezes na frase.")
print("=" * 70, '\n')

# Desenvolva um jogo da forca. Considere que o programa já leu do arquivo uma 
# palavra e está com essa palavra guardada em uma variável. O jogo deve pedir ao 
# usuário uma letra por vez. O jogador poderá errar 6 vezes antes de ser enforcado.

palavra = "CACHORRO"
letras_escolhidas = ""
output = ""
erros = 0
print("======JOGO DA FORCA======")

while erros <= 6 and palavra != output:
    letra = input("Digite uma letra: ").strip().upper()
    while len(letra) != 1:
        print("Valor inválido, digite APENAS uma letra.\n")
        letra = input("Digite uma letra: ").upper().strip()

    if letra not in palavra:
        erros += 1
        print(f"--> Você errou pela {erros}a vez. Tente de novo.\n")

    else:
        output = ""
        letras_escolhidas += letra
        for i in palavra:
            if i in letras_escolhidas:
                output += i
            else:
                output += "_"
        print(f"A palavra é: {output}\n")

if erros > 6:
    print("Você perdeu o jogo.")
else:
    print("Você ganhou o jogo. Parabéns.")

print("=" * 70, '\n')

# Uma string é utilizada para representar uma das fitas de uma cadeia de DNA. 
# Para tanto, as bases Adenina, Guanina, Citosina, Timina e Uracila são representadas 
# pelas letras A, G, C, T e U, respectivamente. Deseja-se construir um programa que
# dada uma sequência de DNA é fornecida a sequência de RNA-m equivalente de acordo 
# com a transformação indicada na Tabela 1.

DNA = "AGCTAGCTAGCT"
RNAm = ""

for i in DNA:
    if i == "A":
        RNAm += "U"
    elif i == "G":
        RNAm += "C"
    elif i == "C":
        RNAm += "G"
    elif i == "T":
        RNAm += "A"

print(f"A faixa de RNA do DNA ({DNA}) é: {RNAm}")
