from parser import Parser
from glob import iglob
import os
from graf import Graf

graf = Graf()

def ucitaj_graf():
    global graf
    lista_fajlova = [fajl for fajl in iglob("python-docs/**/*.html", recursive=True)]
    parser = Parser()
    lista = []

    #u mapu dodamo kao kljuc cvor, a linkove kao vrednost
    for fajl in lista_fajlova:
        linkovi, reci = parser.parse(fajl)
        dodaj_cvor = graf.dodaj_cvor(os.path.abspath(fajl), reci) 
        lista.append([dodaj_cvor, linkovi])

    for el in lista:
        for link in el[1]:
            graf.dodaj_granu(el[0], graf.daj_cvor(link))
