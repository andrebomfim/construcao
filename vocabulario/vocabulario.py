"""
www.dicio.com.br
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict, Counter
from dicio import Dicio
import json
import os
import random
import re
import time


def carrega_palavras_frequentes():
    u"""
    """
    arquivo_frequencia = open('../corpus_pt-br/wl_cb_full_1gram.txt',
                              'r', encoding='utf8')
    frequencia_raw = arquivo_frequencia.readlines()
    padrao_frequencia = re.compile(r'([A-záéíóúüâêîûãõ\-_]+)[\s|\t]*([0-9]+)')
    frequencia_palavras = defaultdict(list)
    for f in frequencia_raw:
        pesquisa = re.findall(padrao_frequencia, f.lower())
        try:
            palavra = pesquisa[0][0]
            frequencia = int(pesquisa[0][1])
            frequencia_palavras[palavra].append(frequencia)
        except IndexError:
            pass
    return frequencia_palavras


def cria_vocabulario(lista_palavras):
    u"""
    """
    vocabulario = dict()
    dicio = Dicio()
    for k, v in lista_palavras.items():
        dicio_palavra = dict()
        try:
            w = dicio.search(k)
            dicio_palavra = {'etimologia': w.etymology,
                             'exemplos': w.examples,
                             'frequencia_pt-br': sum(v),
                             'significado': w.meaning,
                             'sinonimos': w.synonyms,
                             'url': w.url}
            for chave, valor in w.extra.items():
                dicio_palavra = {chave.lower(): valor}
        vocabulario[w.word] = dicio_palavra
        time.sleep(random.randint(4, 10))
    return vocabulario


def salva_vocabulario(vocabulario):
    u"""
    """
    with open('./vocabulario_dicio.json', 'w', encoding='utf8') as arquivo:
        json.dump(vocabulario, arquivo)



if __name__ == '__main__':
    lista_palavras = carrega_palavras_frequentes()
    vocabulario = cria_vocabulario(lista_palavras)
    salva_vocabulario(vocabulario)
