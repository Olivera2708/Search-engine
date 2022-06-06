import random

kraj_boje = "\033[0m"
siva = "\033[93m"
crvena = "\033[31m"
podvuceno = "\033[4m"
plava = "\033[36m"
bela = "\033[37m"

def ispisi(sortirana, reci, top = 5):
    global kraj_boje, siva, crvena, podvuceno, plava, bela, tamno_plava
    brojac = 0
    if sortirana[0][0] > 0:
        brojac += 1
        print("\n-----Nabolji rezultat-----\n")
        print(f"{bela}{brojac}. {plava}{podvuceno}{sortirana[0][1].daj_stranu().daj_putanju()}{kraj_boje} {siva}---->{kraj_boje} {plava}{sortirana[0][0]} rang{kraj_boje}\n\n")
        prikaz_najboljeg(sortirana[0][1], reci)
        print("\n\n-----Ostali-----\n")
        for evaluacija in sortirana[1:]:
            if brojac == top:
                break
            brojac += 1
            if evaluacija[0] > 0:
                print(f"{bela}{brojac}. {plava}{podvuceno}{evaluacija[1].daj_stranu().daj_putanju()}{kraj_boje} {siva}---->{kraj_boje} {plava}{evaluacija[0]} rang{kraj_boje}")
        kraj = False
        if len(sortirana) > 5:
            while not kraj and sortirana[brojac:] != []:
                unos = input("Pritisnite enter za izlistavanje jos rezultata ili 'q' za izlazak -> ")
                if unos == "q":
                    return 0
                elif unos == "":
                    prikazi_jos_5(sortirana[brojac:])
                    brojac += 5
                else:
                    print("Potrebno je pritisnuti enter ili 'q'")
    else:
        print("Ta rec se ne nalazi ni u jednom fajlu na zadatoj putanji")

def prikazi_jos_5(sortirana, top = 5):
    global kraj_boje, bela, plava, podvuceno, siva
    brojac = 0
    for evaluacija in sortirana:
            if brojac == top:
                break
            brojac += 1
            if evaluacija[0] > 0:
                print(f"{bela}{brojac}. {plava}{podvuceno}{evaluacija[1].daj_stranu().daj_putanju()}{kraj_boje} {siva}---->{kraj_boje} {plava}{evaluacija[0]} rang{kraj_boje}")

def prikaz_najboljeg(evaluacija, reci):
    global bela, crvena, kraj_boje
    strana = evaluacija.daj_stranu()
    pozicije = []
    for rec in reci:
        pozicije.extend(strana.daj_trie().daj_pozicije_reci(rec.strip()))
    sve_reci = strana.daj_reci()
    pocetak = pozicije[0]
    broj = random.randint(0, 10)
    for i in range(len(pozicije)-1):
        if pozicije[i + 1] - pozicije[i] < 70:
            pocetak = pozicije[i]
            break
    if pocetak - broj >= 0:
        pocetak = pocetak-broj
    print(sve_reci[pozicije[0]])
    print(pozicije)
    for rec in sve_reci[pocetak: pocetak + 60]:
        for trazi in reci:
            if trazi.strip().lower() == rec.lower():
                print(f"{crvena}{rec}{kraj_boje} ", end="")
            else:
                print(f"{bela}{rec}{kraj_boje} ", end="")  
