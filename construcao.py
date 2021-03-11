"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import datetime
import json
from pprint import pprint
import random
import re


random.seed(datetime.now())

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


def carrega_vocabulario():
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
    vocabulario_prop = list()
    # dicionario_proparoxitonas = dict()
    for j in json_proparoxitonas:
        vocabulario_prop.append(' ' + j['palavra'])
        """
        dicionario_proparoxitonas['palavra'] = {'id': j['id'],
                                                'tipo': j['tipo'],
                                                'silabas': j['sílabas'],
                                                'n_silabas': j['qtde_silabas']}
        """
    prop_mais_frequentes = ''
    return vocabulario_prop, prop_mais_frequentes


def coleta_proparoxitonas():
    u"""
    Função para extrair e armazenar as palavras proparoxítonas no fim dos
    versos da primeira parte da canção.

    Retorna uma lista com as palavras.
    """
    padrao_proparoxitona = re.compile(r'\s[\so|a|um\s]*?\w+\n')
    proparoxitonas = re.findall(padrao_proparoxitona,
                                '\n'.join(lista_primeira_parte))
    prop_originais = [str(p).replace('\n', '') for p in proparoxitonas]
    return prop_originais


def limpa_proparoxitonas(prop_originais):
    u"""
    Função para limpar a primeira parte da canção das palavras proparoxítonas
    no fim dos versos.

    Retorna uma lista com a letra sem as proparoxítonas.
    """
    letra_sem_prop = list()
    for n in range(len(lista_primeira_parte) - 1):
        verso_limpo = lista_primeira_parte[n].replace(prop_originais[n], '')
        letra_sem_prop.append(verso_limpo)
    return letra_sem_prop


def carrega_cancioneiro():
    global prop_cancioneiro
    pass


def recompoe_letra(letra_sem_prop, proparoxitonas):
    u"""
    Função para recompor a letra da canção com novas palavras proparoxítonas.

    Retorna o resultado da reconstrução através da variável letra_nova.
    """
    letra_nova = list()
    for verso in letra_sem_prop:
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
        if verso.endswith(' fosse'):
            proparoxitonas.remove(proparoxitona)
            letra_nova.append(str(verso) + proparoxitona)
        elif verso.endswith(' atrapalhando'):
            proparoxitonas.remove(proparoxitona)
            letra_nova.append(str(verso) + proparoxitona)
        else:
            if verso.endswith('passo') and proparoxitona.endswith('a'):
                casa_verso(verso, letra_nova, proparoxitonas)
            elif verso.endswith('pacote') and proparoxitona.endswith('a'):
                casa_verso(verso, letra_nova, proparoxitonas)
            elif verso.endswith('o') and proparoxitona.endswith('música'):
                casa_verso(verso, letra_nova, proparoxitonas)
            elif verso.endswith('o') and proparoxitona.endswith('única'):
                casa_verso(verso, letra_nova, proparoxitonas)
            elif verso.endswith(' e') and proparoxitona.endswith('única'):
                casa_verso(verso, letra_nova, proparoxitonas)
            else:
                proparoxitonas.remove(proparoxitona)
                proparoxitona = proparoxitona.replace(' um ', ' ')
                proparoxitona = proparoxitona.replace(' o ', ' ')
                proparoxitona = proparoxitona.replace(' a ', ' ')
                letra_nova.append(str(verso) + proparoxitona)
    else:
        casa_verso(verso, letra_nova, proparoxitonas)


def reconstrucao(numero):
    u"""
    Função para sintetizar toda a tarefa do script.

    Param: números decimais de 0 a 4.

    Retorna a letra da música, segundo os critérios:
    0: Letra original sem modificações
    1: Letra com rearranjo das proparoxítonas já existentes.
    2: Letra com rearranjo a partir do cancioneiro de Chico Buarque.
    3: Letra com rearranjo a partir das proparoxítonas mais frequentes na
       língua portuguesa.
    4: Letra com rearranjo a partir de quaisquer proparoxítonas.

    Números decimais combinam parte das palavras entre parâmetros distintos.
    Um número 2,6, por exemplo, combina 40% de proparoxítonas do critério 2
    com 60% de proparoxítonas do critério 3, resultando numa versão da letra
    com resultado misturado.
    """
    try:
        dicionario_criterios = {1: prop_originais,
                                2: prop_cancioneiro,
                                3: prop_mais_frequentes,
                                4: vocabulario_prop}
    except NameError:
        carrega_variaveis()
    if type(numero) == int:
        if numero == 0:
            return LETRA_ORIGINAL
            pprint(LETRA_ORIGINAL)
        else:
            letra_nova = recompoe_letra(letra_sem_prop,
                                        dicionario_criterios[numero])
            pprint(letra_nova)
    else:
        lista_1 = dicionario_criterios[numero // 1]
        # carrega a primeira lista de proparoxítonas a partir do número
        # indicado no dicionario de critérios, arredondando para baixo.
        lista_2 = dicionario_criterios[(numero // 1) + 1]
        # carrega a segunda lista de proparoxítonas a partir do número
        # indicado no dicionario de critérios, arredondando para cima.
        numero_intervalo = numero % 1
        numero_lista_2 = round(numero_intervalo * 41)
        numero_lista_1 = 41 - numero_lista_2
        proparoxitonas = list()
        for n in range(numero_lista_1):
            proparoxitonas.append(random.choice(lista_1))
        for n in range(numero_lista_2):
            proparoxitonas.append(random.choice(lista_2))
        letra_nova = recompoe_letra()
        pprint(letra_nova)


vocabulario_prop, prop_mais_frequentes = carrega_vocabulario()
prop_originais = coleta_proparoxitonas()
letra_sem_prop = limpa_proparoxitonas(prop_originais)
prop_cancioneiro = carrega_cancioneiro()


if __name__ == '__main__':
    reconstrucao(1)
