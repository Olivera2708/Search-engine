from ucitaj_graf import ucitaj_graf
from izracunaj_vrednost import daj_sve_cvorove, sredi_unos

trenutni_cvorovi = []

def ispisi_pocetne_mogucnosti():
    global trenutni_cvorovi
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
                trenutni_cvorovi = za_pretraziti[1]
            sredi_unos(rec, trenutni_cvorovi)
            ispisi_mogucnosti()
            return False
    else:
        return True


def ispisi_mogucnosti():
    global trenutni_cvorovi
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
        #uradi
        dobro = False
        while not dobro:
            rec = input("Unesite rec za pretragu -> ")
            dobro = True
        sredi_unos(rec, trenutni_cvorovi)
        ispisi_mogucnosti()
        return False
    elif izabrano == "2":
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
            trenutni_cvorovi = za_pretraziti[1]
            sredi_unos(rec, trenutni_cvorovi)
            ispisi_mogucnosti()
            return False
    else:
        raise SystemExit(0)


def start():
    #parsiraj fajlove
    ucitaj_graf()
    #pokreni
    kraj = False
    while not kraj:
        kraj = ispisi_pocetne_mogucnosti();

start();