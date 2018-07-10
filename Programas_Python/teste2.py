#!/usr/bin/python3
'''

#Para preenchimento de um arquivo novo

ref_arquivo = open('orig.txt','r')
texto=[]

texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('Maria das Dores')

ref_arquivo.writelines(texto)
ref_arquivo.close()


arquivo = open('orig.txt', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
conteudo.append('\nNova linha')   # insira seu conteúdo

arquivo = open('orig.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()
'''

from datetime import datetime

now = datetime.now()

datahoje=[]

datahoje += str(now.day)
datahoje += '/'
datahoje += str(now.month)
datahoje += '/'

print(datahoje)

