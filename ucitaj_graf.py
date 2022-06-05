from hashmap import HashMap, LinearHashMap
from parser import Parser
from glob import iglob
import os
from graf import Graf
from trie import Trie
from timeit import default_timer as timer

graf = Graf()

def ucitaj_graf():
    global graf
    lista_fajlova = [fajl for fajl in iglob("python-docs/**/*.html", recursive=True)]
    parser = Parser()
    # hash_map = LinearHashMap(capacity=int(len(lista_fajlova)*0.75 + 1))
    lista = []

    #u mapu dodamo kao kljuc cvor, a linkove kao vrednost
    for fajl in lista_fajlova:
        linkovi, reci = parser.parse(fajl)
        start = timer()
        trie = Trie(reci)
        end = timer()
        print(f"Vreme je {end-start} za {len(reci)}")
        dodaj_cvor = graf.dodaj_cvor(os.path.abspath(fajl), reci)
        lista.append([dodaj_cvor, linkovi])
        # hash_map[dodaj_cvor] = linkovi

    for el in lista:
        for link in el[1]:
            graf.dodaj_granu(el[0], graf.daj_cvor(link))

    # for cvor, linkovi in hash_map:
    #     for link in linkovi:
    #         graf.dodaj_granu(cvor, graf.daj_cvor(link))

ucitaj_graf()
