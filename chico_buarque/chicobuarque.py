"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests


def abre_html(url):
    """
    """
    html = requests.get(url)
    sopa = bs(html.content, 'html.parser')
    return sopa


def lista_musicas(sopa):
    """
    """
    lista_all = sopa.find_all('a')
    lista_hrefs = list()
    for l in lista_all:
        l = l.get('href')
        if l is not None:
            if l.startswith('javascript:wopen('):
                lista_hrefs.append(l)
    prefixo_url = 'http://chicobuarque.com.br/construcao/mestre.asp?pg='
    lista_musicas = list()
    for h in lista_hrefs:
        sufixo_url = h.replace("javascript:wopen('", "")
        sufixo_url = sufixo_url.replace("')'", "").replace("')", "")
        url_musica = prefixo_url + sufixo_url
        lista_musicas.append(url_musica)
    return lista_musicas


def salva_musicas(lista_musicas):
    """
    """
    for m in lista_musicas:
        # https://pythonspot.com/selenium-phantomjs/
        sopa = abre_html(m)
        tabela_html = sopa.find('table')
        linhas_tabela = tabela_html.find_all('td')
        titulo = linhas_tabela[2].text
        letra = linhas_tabela[5].text
        cancao = titulo + '\n\n' + letra
        nome_arquivo = './cancioneiro/' + m.split('=')[-1]
        nome_arquivo = nome_arquivo.replace('.htm', '.txt')
        with open(nome_arquivo, 'w', encoding='utf8') as musica:
            musica.write(cancao)


def chico_buarque():
    url = 'http://chicobuarque.com.br/construcao/menu_alfabetica1.htm'
    sopa = abre_html(url)
    lista_musicas = lista_musicas(sopa)
    salva_musicas(lista_musicas)
