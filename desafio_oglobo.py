# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup


def parse_description(description):
    links = []
    content_description = []
    soup = BeautifulSoup(description, 'html.parser')
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    content_description.append({'type': 'links', 'content': links})

    for img in soup.find_all('img'):
        content_description.append({'type': 'image', 'content': img.get('src')})

    for p in soup.find_all('p'):
        text = p.text.replace('\n', '').replace('\t', '')
        if len(text) > 1:
            content_description.append({'type': 'text', 'content': text})

    return content_description


def crawler():
    url = 'https://revistaautoesporte.globo.com/rss/ultimas/feed.xml'
    response = requests.get(url)
    xml_response = response.content
    root = ET.fromstring(xml_response)
    feed = []
    for child in root.iter('item'):
        item = {}
        title = child.find('title').text
        link = child.find('link').text
        description = child.find('description').text
        item['link'] = link
        item['title'] = title
        new_description = parse_description(description)
        item['description'] = new_description
        feed.append({'item': item})

    binds = {}
    binds['feed'] = feed
    print(json.dumps(binds))
    return binds


if __name__ == '__main__':
    crawler()

