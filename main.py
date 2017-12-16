from urllib import FancyURLopener
from bs4 import BeautifulSoup
import os
import re

def tema(lista_temas, site):
    file = open('site_w/' + site + '.txt', 'r')
    file = file.read()
    dic = {}
    for item in file.split():
        if item in lista_temas:
            dic[item] = file.count(item)
    print dic
    print 'O site '+ site +' trata sobre',''.join(dic.keys()[0]),'\n'


def site_a(site):
    if site[0:7] != 'http://':
        site = 'http://' + site
    opener = FancyURLopener()  # criando o 'capturador' de paginas
    page = opener.open(site)  # uma URL de teste
    html = page.read()  # vai se conectar o servidor e capturar o html retornado
    # print html # se quiser ver o html bruto
    soup = BeautifulSoup(html, "lxml")  # limpa as tags de html para deixar apenas o conteudo
    for script in soup(["script", "style"]):
        script.extract()  # retirando os codigos em Javascript e CSS
    conteudo = soup.get_text()

    limpa = ['com', 'br', 'www', 'http']
    site = re.sub(r'[^\w]', " ", site).split()
    novo_site = ''
    for a in site:
        if a not in limpa:
            novo_site += a
    site = novo_site
    file = open('site_w/' + site + '.txt', 'w')
    file.write((conteudo.encode('utf-8')).lower())  # imprime o texto limpo (sem tags html, Javascript ou CSS)
    lista_temas = {'esporte':('futebol', 'bola', 'jogador', 'esporte', 'flamengo', 'vasco', 'botafogo', 'fluminense', 'sport'),
                   'engenharia':('engenharia', 'engenharias', 'engineer'),
                   'jogos': ('jogo', 'jogos', 'game', 'games')}
    tema(lista_temas, site)


lista = raw_input('Deseja analisar uma lista de sites? ')
if lista == 'sim':
    where = raw_input('Onde se encontra o arquivo? ')
    file = open(where, 'r')
    for site in file:
        site_a(site)
else:
    site = raw_input('Digite o site que deseja pesquisar: ')
    site_a(site)
