senha = list(input())
min_caracteres = 6
digito, minusculo, maiusculo, simbolo, falta = 0, 0, 0, 0, 0
i = 0

while i != len(senha): #laço para comparar todas as posições da string
    for c in range(48, 58):
        if senha[i] == chr(c): #comparando string com números na tabela ASCII
            digito += 1
    for c in range(97, 123): #comparando string com letras minúsculas na tabela ASCII
        if senha[i] == chr(c):
            minusculo += 1
    for c in range(65, 91): #comparando string com letras maiúsculas na tabela ASCII
        if senha[i] == chr(c):
            maiusculo += 1
    for c in range(33, 46): #comparando string com símbolos na tabela ASCII
        if senha[i] == chr(c):
            simbolo += 1
        if senha [i] == chr(64): #código do arroba na tabela ASCII
            simbolo +=1
        if senha [i] == chr(94): #código do acento cincunflexo na tabela ASCII
            simbolo +=1
    i += 1

#se for maior que zero, significa que satisfaz os critérios exigidos
#se for menor que zero, significa que falta o(s) caractere(s) daquela(s) classe(s)
if digito == 0: 
    falta += 1
if minusculo == 0: 
    falta += 1
if maiusculo == 0: 
    falta += 1
if simbolo == 0: 
    falta += 1

#somando classe(s) que falta(m) para iterar no laço somente a
#quantidade para atingir o mínimo de caracteres exigidos para senha
quant_senha = len(senha) + falta 

while quant_senha < min_caracteres:
    falta += 1
    quant_senha += 1
    
print(falta)