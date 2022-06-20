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

    
def sredi_unos(rec, za_pretraziti):
    rec = rec.strip()
    if "\"" in rec:
        reci = rec.replace("\"", "").strip().split()
        if len(reci) > 1:
            odredi_rang_izraza(reci, za_pretraziti)
        else:
            odredi_rang_rec(reci[0], za_pretraziti)
    elif " AND " in rec:
        lista_reci = rec.split(" ");
        if len(lista_reci) == 3:
            los = False
            for el in lista_reci:
                if el == "":
                    los = True
                    print("Los unos")
                    break
            reci = rec.split(" AND ")
            if not los:
                odredi_rang_and(rec.split(" AND "), za_pretraziti)
        else:
            print("Los unos")
    elif " NOT " in rec:
        lista_reci = rec.split(" ");
        if len(lista_reci) == 3:
            los = False
            for el in lista_reci:
                if el == "":
                    los = True
                    print("Los unos")
                    break
            if not los:
                odredi_rang_not(rec.split(" NOT "), za_pretraziti)
        else:
            print("Los unos")
    elif " OR " in rec:
        lista_reci = rec.split(" ");
        if len(lista_reci) == 3:
            los = False
            for el in lista_reci:
                if el == "":
                    los = True
                    print("Los unos")
                    break
            if not los:
                odredi_rang_reci(rec.split(" OR "), za_pretraziti)
        else:
            print("Los unos")
    elif " " in rec:
        odredi_rang_reci(rec.split(" "), za_pretraziti)
    else:
        odredi_rang_rec(rec, za_pretraziti)

def odredi_rang_not(lista_reci, za_pretraziti):
    lista_evaluacija = []
    for strana in za_pretraziti:
        br_pojavljivanja1 = broj_pojavljivanja(strana, lista_reci[0].strip())
        br_pojavljivanja2 = broj_pojavljivanja(strana, lista_reci[1].strip())
        if (br_pojavljivanja1 == 0):
            continue
        elif (br_pojavljivanja2 == 0):
            vrednost = br_pojavljivanja1 + bitna_linkovanja(strana, lista_reci[0].strip(), za_pretraziti) + broj_linkovanja(strana)
            lista_evaluacija.append([vrednost, Evaluacija(strana, vrednost)])
    if lista_evaluacija == []:
        print("Ne postoji fajl koji sadzi prvu rec a ne sadrzi drugu rec")
    else:
        sortirana = sort(lista_evaluacija)
        ispisi(sortirana, lista_reci)

def odredi_rang_and(lista_reci, za_pretraziti):
    lista_evaluacija = []
    for strana in za_pretraziti:
        br_pojavljivanja1 = broj_pojavljivanja(strana, lista_reci[0].strip())
        if br_pojavljivanja1 == 0:
            continue
        br_pojavljivanja2 = broj_pojavljivanja(strana, lista_reci[1].strip())
        if br_pojavljivanja2 == 0:
            continue
        else:
            vrednost1 = br_pojavljivanja1 + bitna_linkovanja(strana, lista_reci[0].strip(), za_pretraziti)
            vrednost = vrednost1 + broj_linkovanja(strana)
        lista_evaluacija.append([vrednost, Evaluacija(strana, vrednost)])
    if lista_evaluacija == []:
        print("Ne postoji fajl koji sadzi obe reci")
    else:
        sortirana = sort(lista_evaluacija)
        ispisi(sortirana, lista_reci)

def odredi_rang_reci(lista_reci, za_pretraziti):
    lista_evaluacija = []
    for strana in za_pretraziti:
        br_pojavljivanja = 0
        bit_linkovanja = 0
        for rec in lista_reci:
            br_pojavljivanja += broj_pojavljivanja(strana, rec)
            bit_linkovanja += bitna_linkovanja(strana, rec, za_pretraziti)
        if br_pojavljivanja == 0:
            continue
        else:
            vrednost = br_pojavljivanja//len(lista_reci) + broj_linkovanja(strana) + bit_linkovanja//len(lista_reci)
        lista_evaluacija.append([vrednost, Evaluacija(strana, vrednost)])
    if lista_evaluacija == []:
        print("Reci ne postoje u zadatom direktorijumu")
    else:
        sortirana = sort(lista_evaluacija)
        ispisi(sortirana, lista_reci)

def odredi_rang_rec(rec, za_pretraziti):
    lista_evaluacija = []
    for strana in za_pretraziti:
        br_pojavljivanja = broj_pojavljivanja(strana, rec)
        if br_pojavljivanja == 0:
            continue
        else:
            vrednost = broj_pojavljivanja(strana, rec) + broj_linkovanja(strana) + bitna_linkovanja(strana, rec, za_pretraziti)
        lista_evaluacija.append([vrednost, Evaluacija(strana, vrednost)])
    if lista_evaluacija == []:
        print("Rec ne postoji u zadatom direktorijumu")
    else:
        sortirana = sort(lista_evaluacija)
        ispisi(sortirana, [rec])


def daj_sve_cvorove(putanja):
    if "/Volumes/SSD/Fakultet/Semestar 2/Algoritmi i strukture podataka/Projekat2/python-docs" not in putanja:
        print("Morate izabrati direktorijum unutar python-docs")
        return False, []
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

def bitna_linkovanja(strana, rec, za_pretraziti):
    ukupno = 0
    sve_koje_linkuju = ucitaj_graf.graf.grane_dolaze(strana)
    for s in sve_koje_linkuju:
        if s in za_pretraziti:
            ukupno += broj_pojavljivanja(s, rec)
    return ukupno//8




########BONUS##########
def odredi_rang_izraza(lista_reci, za_pretraziti):
    lista_evaluacija = []
    for strana in za_pretraziti:
        pozicije = pozicije_pojavljivanja(strana, lista_reci)
        broj_pojavljivanja = len(pozicije)
        if broj_pojavljivanja == 0:
            continue
        bit_linkovanja = bitna_linkovanja_izraza(strana, lista_reci, za_pretraziti)
        ukupno = broj_pojavljivanja * 5 + bit_linkovanja + broj_linkovanja(strana)
        lista_evaluacija.append([ukupno, Evaluacija(strana, ukupno), pozicije])
    if lista_evaluacija == []:
        print("Rec ne postoji u zadatom direktorijumu")
    else:
        sortirana = sort(lista_evaluacija)
        ispisi(sortirana, lista_reci, dodatni=True)

def pozicije_pojavljivanja(strana, lista_reci):
    lista_pojavljivanja = []
    for rec in lista_reci:
        lista = strana.daj_trie().daj_pozicije_reci(rec.strip())
        if lista == []:
            return []
        else:
            lista_pojavljivanja.append(lista)
    else:
        return broj_pojavljivanja_izraza(lista_pojavljivanja)

def bitna_linkovanja_izraza(strana, lista_reci, za_pretraziti):
    ukupno = 0
    sve_koje_linkuju = ucitaj_graf.graf.grane_dolaze(strana)
    for s in sve_koje_linkuju:
        if s in za_pretraziti:
            ukupno += len(pozicije_pojavljivanja(s, lista_reci))
    return ukupno//2

def broj_pojavljivanja_izraza(lista_pojavljivanja):
    pozicija = []
    for br in lista_pojavljivanja[0]:
        if sledeci(br, lista_pojavljivanja[1:]):
            pozicija.append(br)
    return pozicija

def sledeci(broj, lista):
    if len(lista) == 1 and broj + 1 in lista[0]:
        return True
    if broj + 1 in lista[0]:
        return True and sledeci(broj+1, lista[1:])
    return False
