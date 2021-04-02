"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict, Counter
from datetime import datetime
import json
import os
import re


LETRA_ORIGINAL = '''Amou daquela vez como se fosse a última
Beijou sua mulher como se fosse a última
E cada filho seu como se fosse o único
E atravessou a rua com seu passo tímido
Subiu a construção como se fosse máquina
Ergueu no patamar quatro paredes sólidas
Tijolo com tijolo num desenho mágico
Seus olhos embotados de cimento e lágrima
Sentou pra descansar como se fosse sábado
Comeu feijão com arroz como se fosse um príncipe
Bebeu e soluçou como se fosse um náufrago
Dançou e gargalhou como se ouvisse música
E tropeçou no céu como se fosse um bêbado
E flutuou no ar como se fosse um pássaro
E se acabou no chão feito um pacote flácido
Agonizou no meio do passeio público
Morreu na contramão atrapalhando o tráfego
Amou daquela vez como se fosse o último
Beijou sua mulher como se fosse a única
E cada filho seu como se fosse o pródigo
E atravessou a rua com seu passo bêbado
Subiu a construção como se fosse sólido
Ergueu no patamar quatro paredes mágicas
Tijolo com tijolo num desenho lógico
Seus olhos embotados de cimento e tráfego
Sentou pra descansar como se fosse um príncipe
Comeu feijão com arroz como se fosse o máximo
Bebeu e soluçou como se fosse máquina
Dançou e gargalhou como se fosse o próximo
E tropeçou no céu como se ouvisse música
E flutuou no ar como se fosse sábado
E se acabou no chão feito um pacote tímido
Agonizou no meio do passeio náufrago
Morreu na contramão atrapalhando o público
Amou daquela vez como se fosse máquina
Beijou sua mulher como se fosse lógico
Ergueu no patamar quatro paredes flácidas
Sentou pra descansar como se fosse um pássaro
E flutuou no ar como se fosse um príncipe
E se acabou no chão feito um pacote bêbado
Morreu na contramão atrapalhando o sábado
Por esse pão pra comer, por esse chão pra dormir
A certidão pra nascer e a concessão pra sorrir
Por me deixar respirar, por me deixar existir, Deus lhe pague
Pela cachaça de graça que a gente tem que engolir
Pela fumaça e a desgraça, que a gente tem que tossir
Pelos andaimes pingentes que a gente tem que cair,
Deus lhe pague
Pela mulher carpideira pra nos louvar e cuspir
E pelas moscas bicheiras a nos beijar e cobrir
E pela paz derradeira que enfim vai nos redimir, Deus lhe pague'''

lista_letra_original = LETRA_ORIGINAL.split('\n')
lista_primeira_parte = lista_letra_original[0:41]
lista_segunda_parte = lista_letra_original[41:]


def carrega_cancioneiro():
    u"""
    """
    lista_cancioneiro = list()
    os.chdir('../bases/chico_buarque/cancioneiro/')
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
    os.chdir('../../../')
    return cancioneiro


def carrega_vocabulario(cancioneiro):
    u"""
    Função para carregar as proparoxítonas presentes no acervo de palavras.

    O arquivo de vocabulário foi retirado do Portal da Língua Portuguesa
    (portaldalinguaportuguesa.org).

    Retorna uma lista contendo dicionário com as palavras, id, tipo, separação
    silábica e quantidade de sílabas.
    """
    arquivo_proparoxitonas = open('./bases/vocabulario/proparoxitonas_dicio.json',
                                  'r', encoding='utf8')
    vocabulario = json.load(arquivo_proparoxitonas)
    lista_vocabulario = []
    for v in vocabulario:
        lista_vocabulario.append(v)
    for l in lista_vocabulario:
        vocabulario[l]['frequencia_chico'] = cancioneiro.get(vocabulario[l]['palavra'], 0)
    # gera um dicionário contendo as palavras como chaves e os itens do
    # vocabulário como pares.
    arquivo_proparoxitonas.close()
    # with open('../vocabulario_prop.json', 'w', encoding='utf8') as v_json:
    #     json.dump(vocabulario, v_json)
    return vocabulario


def coleta_proparoxitonas(vocabulario):
    u"""
    Função para extrair e armazenar as palavras proparoxítonas no fim dos
    versos da primeira parte da canção.

    Retorna uma lista com as palavras.
    """
    padrao_proparoxitona = re.compile(r'\s[\so|a|um\s]*?\w+\n')
    proparoxitonas = re.findall(padrao_proparoxitona,
                                '\n'.join(lista_primeira_parte))
    prop_originais = [str(p).replace('\n', '') for p in proparoxitonas]
    p_o_counter = [p.replace(' um ', '').replace(' o ', '').strip() for p in prop_originais]
    freq_prop_originais = Counter(p_o_counter)
    lista_vocabulario = []
    for v in vocabulario:
        lista_vocabulario.append(v)
    for l in lista_vocabulario:
        vocabulario[l]['frequencia_construcao'] = freq_prop_originais.get(l, 0)
    return vocabulario
    with open('./bases/proparoxitonas/proparoxitonas_vocabulario.json',
              'w', encoding='utf8') as arquivo_json:
        json.dump(vocabulario, arquivo_json)


def grava_proparoxitonas(vocabulario):
    prop_originais = dict()
    prop_cancioneiro = dict()
    for k, v in vocabulario.items():
        if vocabulario[k]['frequencia_construcao'] > 0:
            prop_originais[k] = v
        if vocabulario[k]['frequencia_chico'] > 0:
            prop_cancioneiro[k] = v
    with open('./proparoxitonas/proparoxitonas_construcao.json',
              'w', encoding='utf8') as arquivo_construcao:
        json.dump(prop_originais, arquivo_construcao)
    with open('./proparoxitonas/proparoxitonas_cancioneiro.json',
              'w', encoding='utf8') as arquivo_cancioneiro:
        json.dump(prop_cancioneiro, arquivo_cancioneiro)
    with open('./proparoxitonas/proparoxitonas.json',
              'w', encoding='utf8') as arquivo_proparoxitonas:
        json.dump(vocabulario, arquivo_proparoxitonas)


def proparoxitonas():
    cancioneiro = carrega_cancioneiro()
    vocabulario = carrega_vocabulario(cancioneiro)
    vocabulario = coleta_proparoxitonas(vocabulario)
    grava_proparoxitonas(vocabulario)


if __name__ == '__main__':
    proparoxitonas()
