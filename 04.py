
from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"


site_connect = Scrapy_Table(url)

tables = site_connect.get_tables(5)
  
total = 0 

for linha in tables[1:]:

    nome = linha[0]

    l_nome  = nome.split(" ")
         
    if 'jos�' == l_nome[0].lower():
        print(nome)
          
    if 'eduardo' == l_nome[0].lower():
        print(nome)

    if 'jo�o' == l_nome[0].lower():
        print(nome)

