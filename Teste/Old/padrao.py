#!/usr/bin/python3

vetor = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

i=0
contCon=0
contVog=0

while i <= 9:
    if vetor[i] not in 'aeiou':
        contCon += 1
    if vetor[i] in 'aeiou':
        contVog += 1

    i += 1

print("Lidos %d:consoantes e %d:vogais em um vetor com %d:Letras" % (contCon, contVog, len(vetor)))