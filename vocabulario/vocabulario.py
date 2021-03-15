from collections import defaultdict, Counter
import json
import os
import re


def carrega_cancioneiro():
    u"""
    """
    lista_cancioneiro = list()
    os.chdir('./chico_buarque/cancioneiro/')
    for t in os.listdir():
        if t.endswith('_titulo.txt'):
            pass
        else:
            with open(t, 'r', encoding='utf8') as arquivo_letra:
                letra = arquivo_letra.read()
                letra = letra.replace('\n', ' ')
                letra = letra.split('©')[0]
                palavras = letra.split()
                for palavra in palavras:
                    lista_cancioneiro.append(palavra.lower())
    cancioneiro = Counter(lista_cancioneiro)
    os.chdir('../../')
    return cancioneiro


def carrega_vocabulario(cancioneiro):
    u"""
    Função para carregar as proparoxítonas presentes no acervo de palavras.

    O arquivo de vocabulário foi retirado do Portal da Língua Portuguesa
    (portaldalinguaportuguesa.org).

    Retorna uma lista contendo dicionário com as palavras, id, tipo, separação
    silábica e quantidade de sílabas.
    """
    arquivo_proparoxitonas = open('./vocabulario/proparoxitonas.json',
                                  'r', encoding='utf8')
    json_proparoxitonas = json.load(arquivo_proparoxitonas)
    arquivo_frequencia = open('./corpus_pt-br/wl_cb_full_1gram.txt',
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
    vocabulario = defaultdict(list)
    for j in json_proparoxitonas:
        try:
            j['frequencia_pt'] = sum(frequencia_palavras.get(j['palavra'], 0))
        except TypeError:
            j['frequencia_pt'] = frequencia_palavras.get(j['palavra'], 0)
        j['frequencia_chico'] = cancioneiro.get(j['palavra'], 0)
        vocabulario[j['palavra']].append(j)
    # gera um dicionário contendo as palavras como chaves e os itens do
    # vocabulário como pares.
    arquivo_proparoxitonas.close()
    arquivo_frequencia.close()
    with open('./vocabulario_prop.json', 'w', encoding='utf8') as v_json:
        json.dump(vocabulario, v_json)
    return vocabulario
