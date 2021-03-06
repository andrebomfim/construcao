"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from pprint import pprint
import random
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


def coleta_proparoxitonas():
    u"""
    Função para extrair e armazenar as palavras proparoxítonas no fim dos
    versos da primeira parte da canção.

    Retorna uma lista com as palavras.
    """
    padrao_proparoxitona = re.compile(r'\s[\so|a|um\s]*?\w+\n')
    proparoxitonas = re.findall(padrao_proparoxitona,
                                '\n'.join(lista_primeira_parte))
    proparoxitonas = [str(p).replace('\n', '') for p in proparoxitonas]
    return proparoxitonas


def limpa_proparoxitonas(proparoxitonas):
    u"""
    Função para limpar a primeira parte da canção das palavras proparoxítonas
    no fim dos versos.

    Retorna uma lista com a letra sem as proparoxítonas.
    """
    letra_sem_proparoxitonas = list()
    for n in range(len(lista_primeira_parte) - 1):
        verso_limpo = lista_primeira_parte[n].replace(proparoxitonas[n], '')
        letra_sem_proparoxitonas.append(verso_limpo)
    return letra_sem_proparoxitonas


def recompoe_letra(letra_sem_proparoxitonas, proparoxitonas):
    u"""
    Função para recompor a letra da canção com novas palavras proparoxítonas.

    Retorna o resultado da reconstrução através da variável letra_nova.
    """
    letra_nova = list()
    for verso in letra_sem_proparoxitonas:
        casa_verso(verso, letra_nova, proparoxitonas)
    letra_nova = '\n'.join(letra_nova) + '\n' +\
                 '\n'.join(lista_segunda_parte)
    return letra_nova


def casa_verso(verso, letra_nova, proparoxitonas):
    u"""
    Função para recompor cada verso com uma palavra proparoxítona.

    Retorna um verso reconstruído para a variável lista_nova.
    """
    proparoxitona = random.choice(proparoxitonas)
    if verso.endswith('s') and proparoxitona.endswith('s'):
        proparoxitonas.remove(proparoxitona)
        letra_nova.append(str(verso) + proparoxitona)
    elif not verso.endswith('s') and not proparoxitona.endswith('s'):
        proparoxitonas.remove(proparoxitona)
        letra_nova.append(str(verso) + proparoxitona)
    else:
        casa_verso(verso, letra_nova, proparoxitonas)


def reconstrucao_interna():
    u"""
    Função para sintetizar toda a tarefa do script.

    Retorna a letra nova da canção recombinando as proparoxítonas
    que já existiam na letra.
    """
    proparoxitonas = coleta_proparoxitonas()
    letra_sem_proparoxitonas = limpa_proparoxitonas(proparoxitonas)
    letra_nova = recompoe_letra(letra_sem_proparoxitonas, proparoxitonas)
    return letra_nova
    pprint(letra_nova)


def reconstrucao_externa():
    u"""
    Função para sintetizar toda a tarefa do script.

    Retorna a letra nova da canção utilizando proparoxítonas retiradas do
    Portal da Língua Portuguesa (portaldalinguaportuguesa.org).
    """
    arquivo_proparoxitonas = open('proparoxitonas.json', 'r', encoding='utf8')
    json_proparoxitonas = json.load(arquivo_proparoxitonas)
    vocabulario_proparoxitonas = list()
    for j in json_proparoxitonas:
        vocabulario_proparoxitonas.append(' ' + j['palavra'])
    proparoxitonas = coleta_proparoxitonas()
    letra_sem_proparoxitonas = limpa_proparoxitonas(proparoxitonas)
    letra_nova = recompoe_letra(letra_sem_proparoxitonas,
                                vocabulario_proparoxitonas)
    return letra_nova
    pprint(letra_nova)


if __name__ == '__main__':
    pass
