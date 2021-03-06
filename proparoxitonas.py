"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json


def carrega_vocabulario(arquivo_vocabulario):
    """
    Função para carregar o arquivo csv contendo o vocabulário de Portugues.
    """
    with open(arquivo_vocabulario, 'r', newline='\n', encoding='utf8')\
            as vocabulario_raw:
        vocabulario = list(csv.DictReader(vocabulario_raw))
        return vocabulario


def gera_proparoxitonas(vocabulario):
    """
    """
    ACENTO = list('áéíóúâêîôûãõ')
    proparoxitonas = list()
    for v in vocabulario:
        lista_silabas = v['sílabas'].replace('-', '·').split('·')
        qtde_silabas = len(lista_silabas)
        v['qtde_silabas'] = qtde_silabas
        if v['qtde_silabas'] == 3:
            for a in ACENTO:
                if a in lista_silabas[0]:
                    proparoxitonas.append(v)
    return proparoxitonas


def proparoxitonas():
    """
    """
    vocabulario = carrega_vocabulario('./vocabulario.csv')
    proparoxitonas = gera_proparoxitonas(vocabulario)
    with open('./proparoxitonas.json', 'w', encoding='utf8') as arquivo_json:
        json.dump(proparoxitonas, arquivo_json)


if __name__ == '__main__':
    proparoxitonas()
