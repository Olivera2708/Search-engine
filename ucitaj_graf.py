from parser import Parser
from glob import iglob
import os
from graf import Graf

def ucitaj_graf():
    lista_fajlova = [fajl for fajl in iglob("python-docs/**/*.html", recursive=True)]
    graf = Graf()
    parser = Parser()
    maps = {}

    #u mapu dodamo kao kljuc cvor, a linkove kao vrednost
    for fajl in lista_fajlova:
        linkovi, reci = parser.parse(fajl)
        dodaj_cvor = graf.dodaj_cvor(os.path.abspath(fajl), reci)
        maps[dodaj_cvor] = linkovi

    for cvor, linkovi in maps.items():
        for link in linkovi:
            graf.dodaj_ivicu(cvor, graf.daj_cvor(link))

ucitaj_graf()
