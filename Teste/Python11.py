import random

def embaralha(lista):

    lista2 = "/".join(lista)
    lista3 = lista2.split("/")

    random.shuffle(lista3)
    return lista3

a = input("Digite um palavra: ")

print("final",embaralha(a))

## https://www.youtube.com/watch?v=lkF7fwwdn74&index=40&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc
