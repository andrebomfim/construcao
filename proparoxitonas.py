"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
from pprint import pprint


def carrega_vocabulario(arquivo_vocabulario):
    """
    Função para carregar o arquivo csv contendo o vocabulário de Portugues.
    """
    with open(arquivo_vocabulario, 'r', encoding='utf8') as vocabulario:
