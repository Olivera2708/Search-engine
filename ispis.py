def ispisi(sortirana, top = 5):
    brojac = 0
    if sortirana[0][0] > 0:
        print("\n-----Nabolji rezultat-----\n")
        print(f"{sortirana[0][1].daj_stranu().daj_putanju()} ----> {sortirana[0][0]} rang\n\n")
        brojac += 1
        print("-----Ostali-----\n")
        for evaluacija in sortirana[1:]:
            if brojac == top:
                break
            brojac += 1
            if evaluacija[0] > 0:
                print(f"{evaluacija[1].daj_stranu().daj_putanju()} ----> {evaluacija[0]} rang")
        kraj = False
        if len(sortirana) > 5:
            while not kraj and sortirana[brojac:] != []:
                unos = input("Pritisnite enter za prikaz narednih 5 ili 'x' za izlazak -> ")
                if unos == "x":
                    return 0
                elif unos == "":
                    prikazi_jos_5(sortirana[brojac:])
                    brojac += 5
                else:
                    print("Potrebno je pritisnuti enter ili 'x'")
    else:
        print("Ta rec se ne nalazi ni u jednom fajlu na zadatoj putanji")

def prikazi_jos_5(sortirana, top = 5):
    brojac = 0
    for evaluacija in sortirana:
            if brojac == top:
                break
            brojac += 1
            if evaluacija[0] > 0:
                print(f"{evaluacija[1].daj_stranu().daj_putanju()} ----> {evaluacija[0]} rang")
