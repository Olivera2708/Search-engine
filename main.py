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
        #uradi
        return False
    else:
        return True


def ispisi_mogucnosti():
    mogucnosti ='''
---------PRETRAGA---------

1. Nova pretgraga
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
        return False
    elif izabrano == 2:
        return False
    else:
        return True


def start():
    #parsiraj fajlove

    #pokreni
    kraj = False
    while not kraj:
        kraj = ispisi_pocetne_mogucnosti();



start();