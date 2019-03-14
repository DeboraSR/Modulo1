
from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"
url_jato="https://pt.wikipedia.org/wiki/Lista_de_pessoas_envolvidas_na_Opera%C3%A7%C3%A3o_Lava_Jato"

site_vereadores = Scrapy_Table(url)
site_jato       = Scrapy_Table(url_jato)


vereadores      = tuple(site_vereadores.get_tables(5))
lista_lava_jato = tuple(site_jato.get_tables(1))


lista_investigados = ()
for investigados in  lista_lava_jato[1:]:
    lista_investigados = lista_investigados + (investigados[0],)

for vereador in vereadores[1:]:
    # Verifica se o nome do vereador esta na lista de investigados
    if vereador[0] in lista_investigados:
       print(vereador)

