"""

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time


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
    prefixo_url = 'http://chicobuarque.com.br/letras/'
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
    driver = webdriver.Firefox()
    time.sleep(1)
    for m in lista_musicas:
        driver.get(m)
        time.sleep(1)
        sopa = bs(driver.page_source, 'html.parser')
        try:
            tabela_html = sopa.find('table')
            linhas_tabela = tabela_html.find_all('td')
            titulo = linhas_tabela[2].text
            letra = linhas_tabela[5].text
        except AttributeError:
            body = sopa.find('body')
            letra = body.text
        print(m.split('/')[-1])
        nome_arquivo = './cancioneiro/' + m.split('/')[-1]
        nome_arquivo_letra = nome_arquivo.replace('.htm', '.txt')
        nome_arquivo_titulo = nome_arquivo.replace('.htm', '_titulo.txt')
        with open(nome_arquivo_letra, 'w', encoding='utf8') as musica:
            musica.write(letra)
        with open(nome_arquivo_titulo, 'w', encoding='utf8') as metadados:
            metadados.write(titulo)
    driver.close()


def chico_buarque():
    url = 'http://chicobuarque.com.br/construcao/menu_alfabetica1.htm'
    sopa = abre_html(url)
    links_musicas = lista_musicas(sopa)
    salva_musicas(links_musicas)


if __name__ == '__main__':
    chico_buarque()
