import ucitaj_graf
from merge_sort import sort
from glob import iglob
from ispis import ispisi

class Evaluacija:
    def __init__(self, strana, vrednost):
        self._strana = strana
        self._vrednost = vrednost

    def daj_vrednost(self):
        return self._vrednost

    def daj_stranu(self):
        return self._strana

def odredi_rang(rec, za_pretraziti):
    za_pretraziti = za_pretraziti

    lista_evaluacija = []
    for strana in za_pretraziti:
        br_pojavljivanja = broj_pojavljivanja(strana, rec)
        if br_pojavljivanja == 0:
            continue
        else:
            vrednost = broj_pojavljivanja(strana, rec) + broj_linkovanja(strana) + bitna_linkovanja(strana, rec)
        lista_evaluacija.append([vrednost, Evaluacija(strana, vrednost)])
    if lista_evaluacija == []:
        print("Rec ne postoji u zadatom direktorijumu")
    else:
        sortirana = sort(lista_evaluacija)
        ispisi(sortirana)

def daj_sve_cvorove(putanja):
    lista_fajlova = [fajl for fajl in iglob(f"{putanja}/**/*.html", recursive=True)]
    za_pretraziti = [ucitaj_graf.graf.daj_cvor(putanja) for putanja in lista_fajlova] #uzmi samo odredjene cvorove

    if len(za_pretraziti) == 0:
        print("U izabranom direktorijumu nema fajla koji moze da se pretrazi")
        return False, []
    else:
        return True, za_pretraziti


def broj_pojavljivanja(strana, rec):
    try:
        return len(strana.daj_trie().daj_pozicije_reci(rec))
    except:
        return 0

def broj_linkovanja(strana):
    return ucitaj_graf.graf.broj_grana_dolaze(strana)

def bitna_linkovanja(strana, rec):
    ukupno = 0
    sve_koje_linkuju = ucitaj_graf.graf.grane_dolaze(strana)
    for s in sve_koje_linkuju:
        ukupno += broj_pojavljivanja(s, rec)
    return ukupno//8





# class Vrednost:
#     def __init__(self, strana, vrednost, pozicije):
#         self._strana = strana
#         self._vrednost = vrednost
#         self._pozicije = pozicije

#     def vrednost(self):
#         return self._vrednost

#     def pozicije(self):
#         return self._pozicije

#     def strana(self):
#         return self._strana

#     def dodaj_pozicije(self, pozicije):
#         self._pozicije = pozicije

#     def dodaj_vrednost(self, vrednost):
#         self._vrednost = vrednost

# def broj_pojavljivanja(strana, rec):
#     return len(strana.daj_pozicije(rec))

# def broj_linkovanja(strana):
#     return ucitaj_graf.graf.broj_linkovanja(strana)

# def relevantnost_strane(strana, rec):
#     return ucitaj_graf.graf.relevantnost(strana, rec) #vraca recnik

# def vrednost(strana, rec):
#     pojavljivanje = broj_pojavljivanja(strana, rec)
#     linkovanje = broj_linkovanja(strana)
#     relevantnost = relevantnost_strane(strana, rec)

#     v = list(relevantnost.values())
#     k = list(relevantnost.keys())
#     ukupno = pojavljivanje + linkovanje + max(v)
#     print(ukupno)
#     return ukupno

# def pretrazi(rec, ispis = 10):
#     lista_vrednosti = []
#     for strana in ucitaj_graf.graf.cvorovi():
#         ukupno = vrednost(strana, rec)
#         lista_vrednosti.append(Vrednost(strana, ukupno, strana.daj_poziciju_reci(rec)))

#     print(lista_vrednosti)
#     #uradi neki sort pa ispisi prvih 10 npr
