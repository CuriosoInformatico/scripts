#!/usr/bin/env python3
from bs4 import BeautifulSoup
import os.path
import sys

"""

Autor:		Samuel López Saura
Twitter:	@elchicodepython
Version:	0.1
Fecha:		28-04-2017

    Modo de uso: python3 xlinker.py filename url_to_link
    Crea script que se carga de forma remota en la imagen desde la
    url especificada cuando se renderiza en un navegador.
    
    Requísitos del sistema:
    apt-get install libxml2-dev libxslt-dev

requirements.txt
---------------------

beautifulsoup4==4.5.3
bs4==0.0.1
lxml==3.7.3


"""


filename = sys.argv[1]
url = sys.argv[2]

assert os.path.splitext(filename)[1] == '.svg', 'La imagen debe ser svg'

with open(filename) as svg:
    svg_data = svg.read()

soup = BeautifulSoup(svg_data, 'lxml')
svg_tag = soup.select('svg')[0]
svg_tag['xmlns:xlink'] = 'http://www.w3.org/1999/xlink'

newtag = soup.new_tag('script')
newtag['xlink:href'] = sys.argv[2]
svg_tag.append(newtag)


svg_data = soup.prettify()
with open(filename, "w") as file:
    file.write(svg_data)
