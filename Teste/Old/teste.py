#!/usr/bin/python3

import os
import time

def ping(host):

    import subprocess

    args = "ping "+ " " + " -c 1" + " " + host

    try:
        lista_sucesso = subprocess.check_output(args, shell=True)
        return True
    except Exception:
        return False

def tempo(i,h):

    from tqdm import tqdm

    os.system("clear")

    tqdm.write(h)

    pbar = tqdm(total=qhost_out)
    pbar.update(i)
    pbar.close()

def continuo (i,h):
    ff = str(i)
    h += ff

    var.append(ping(h))
    ping(h)
    tempo(i, h)

def concatenacao(a):

    ab = str(a)
    ac = host_padrao
    ac += ab

    return ac

def data ():
    from datetime import datetime

    horaraio_atual = datetime.now()



    return str(horaraio_atual)

def escrita (texto):

    arquivo = open('orig.txt', 'r')
    conteudo = arquivo.readlines()

    conteudo.append("\n IP: -")
    conteudo.append(texto)
    conteudo.append("- ás ")
    conteudo.append(data())

    arquivo = open('orig.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()



qhost_in = int(input("Digite o ip_inicio da busca por host: \n"))

qhost_out = int(input("Digite o ip_fim da busca por host: \n"))

host_padrao = input("Digite o seu host padrão (EX:192.168.0.)")

var=[]
for i in range (qhost_in,qhost_out):
    continuo(i,host_padrao)

for a in range(0, len(var)):
    if (var[a]==True):escrita(concatenacao(a))

os.system("clear")
