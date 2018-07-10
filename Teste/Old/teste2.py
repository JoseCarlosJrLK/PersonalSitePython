#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import timeit

processo = subprocess.Popen(args = ["python3 teste.py"],stdin = subprocess.PIPE,stderr = subprocess.PIPE, shell = True)

inicio = timeit.default_timer()
processo.communicate(b'1 \n 225 \n 10.1.1.')
fim = timeit.default_timer()
print('duracao: %f  seg' % (fim - inicio))
