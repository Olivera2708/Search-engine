from ucitaj_graf import ucitaj_graf
from izracunaj_vrednost import daj_sve_cvorove, odredi_rang
from timeit import default_timer as timer

def ispisi_pocetne_mogucnosti():
    mogucnosti = '''
---------PRETRAGA---------

1. Izaberite direktorijum
2. Izlaz
'''
    print(mogucnosti);
    izabrano = input("Izaberite opciju -> ");
    while izabrano not in ["1", "2"]:
        print("Potrebno je izabrati jednu od ponudjenih opcija")
        izabrano = input("Izaberite opciju -> ");
    if izabrano == "1":
        dobro = False
        while not dobro:
            putanja = input("Unesite putanju za pretragu -> ")
            dobro = True
        za_pretraziti = daj_sve_cvorove(putanja)
        if za_pretraziti[0] == True:
            dobro = False
            while not dobro:
                rec = input("Unesite rec za pretragu -> ")
                dobro = True
            odredi_rang(rec, za_pretraziti[1])
            ispisi_mogucnosti(za_pretraziti[1])
            return False
    else:
        return True


def ispisi_mogucnosti(putanja):
    mogucnosti ='''
---------PRETRAGA---------

1. Nova pretraga
2. Promenite direktorijum
3. Izlaz
'''
    print(mogucnosti);
    izabrano = input("Izaberite opciju -> ");
    while izabrano not in ["1", "2", "3"]:
        print("Potrebno je izabrati jednu od ponudjenih opcija")
        izabrano = input("Izaberite opciju -> ");
    if izabrano == "1":
        putanja = putanja
        #uradi
        dobro = False
        while not dobro:
            rec = input("Unesite rec za pretragu -> ")
            dobro = True
        odredi_rang(rec, putanja)
        ispisi_mogucnosti(putanja)
        return False
    elif izabrano == 2:
        dobro = False
        while not dobro:
            putanja = input("Unesite putanju za pretragu -> ")
            dobro = True
        za_pretraziti = daj_sve_cvorove(putanja)
        if za_pretraziti[0] == True:
            dobro = False
            while not dobro:
                rec = input("Unesite rec za pretragu -> ")
                dobro = True
            odredi_rang(rec, za_pretraziti[1])
            ispisi_mogucnosti(putanja)
            return False
    else:
        return True


def start():
    #parsiraj fajlove
    start = timer()
    ucitaj_graf()
    end = timer()
    print(end-start)
    #pokreni
    kraj = False
    while not kraj:
        kraj = ispisi_pocetne_mogucnosti();

start();