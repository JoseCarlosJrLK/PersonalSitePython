#!/usr/bin/python3

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
    import os

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

def data ():
    from datetime import datetime

    now = datetime.now()

    datahoje=[]

    datahoje.append(now.day)
    datahoje.append('/')
    datahoje.append(now.month)
    datahoje.append('/')
    datahoje.append(now.year)
    datahoje.append(': - ás ')
    datahoje.append(now.hour)
    datahoje.append('h:')
    datahoje.append(now.minute)
    datahoje.append('min')

    return datahoje

def escrita (texto):
    arquivo = open('orig.txt', 'r')
    conteudo = arquivo.readlines()
    conteudo.append("\n IP:")
    print(texto)
    conteudo.append(texto)
    conteudo.append("- ás")
    dt=data()
    print(dt)
    conteudo.append(dt)
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
    if (var[a]==True):
        ab = str(a)
        ac=host_padrao
        ac += ab

        escrita(ac)

print("Processo Concluido!")

