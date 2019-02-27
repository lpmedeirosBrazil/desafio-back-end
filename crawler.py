# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'galleani'

from constants import URL_AUTO_ESPORTE
import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup


""" funcao responsavel por realizar a quebra das tags html da descricao da revista auto esporte"""
def parse_description(description):
    content_description = []
    soup = BeautifulSoup(description, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    content_description.append({'type': 'links', 'content': links})
    content_description.append([{'type': 'image', 'content': link.get('src')} for link in soup.find_all('img')])

    for p in soup.find_all('p'):
        text = p.text.replace('\n', '').replace('\t', '')
        if len(text) > 1:
            content_description.append({'type': 'text', 'content': text})
    return content_description

""" funcao responsavel por realizar a quebra do xml e realizar a montagem do json"""
def scrap_xml(xml_response):
    if xml_response:
        root = ET.fromstring(xml_response)
        feed = []
        for child in root.iter('item'):
            item = {}
            title = child.find('title').text
            link = child.find('link').text
            description = child.find('description').text
            item['link'] = link
            item['title'] = title
            item['description'] = parse_description(description)
            feed.append({'item': item})
        crawler_feed = {'feed': feed}
    else:
        crawler_feed = {'feed':'error'}
    return crawler_feed

""" funcao responsavel por realizar a requisicao e realizar a chamada das demais funções para montar o json da resposta"""
def get_auto_esporte():
    url = URL_AUTO_ESPORTE
    response = requests.get(url)
    xml_response = response.content if response.status_code == 200 else None
    crawler_feed = scrap_xml(xml_response)
    return crawler_feed


""" descomente as linhas abaixos para testar e visualizar os dados retornados do crawler"""
if __name__ == '__main__':
    feed = get_auto_esporte()
    import json
    print(json.dumps(feed, indent=4))

