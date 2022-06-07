from hashmap import HashMap, LinearHashMap

class Trie:
    class Cvor:
        def __init__(self, karakter = "", dubina = 0):
            self._karakter = karakter
            #cuvam pozicije [pozicija, vrednost] - vrednost je True ili False, da li je kraj reci
            self._pozicije = []
            #cuvam kljuc karakter, vrednost cvor
            if dubina == 0:
                self._deca = LinearHashMap(90)
            if dubina == 1:
                self._deca = LinearHashMap(24)
            else:
                self._deca = LinearHashMap(5)

        def daj_karakter(self):
            return self._karakter

        def daj_decu(self):
            return self._deca

        def dodaj_dete(self, cvor):
            self._deca[cvor.daj_karakter()] = cvor

        def daj_pozicije(self):
            return self._pozicije

        def dodaj_poziciju(self, pozicija, kraj):
            self._pozicije.append([pozicija, kraj])

        def daj_cvor(self, slovo):
            return self._deca[slovo]

    def __init__(self, reci):
        self._koren = self.Cvor()
        self._reci = reci
        self._dodaj_reci()

####TEST
    def daj_koren(self):
        return self._koren
        #####

    def _dodaj_reci(self):
        for pozicija in range(len(self._reci)):
            self._dodaj(self._reci[pozicija].lower(), pozicija)

    def _dodaj(self, rec, pozicija):
        trenutni_cvor = self._koren
        for index in range(len(rec)):
            kraj = False
            if index == len(rec)-1:
                kraj = True
            if rec[index] in trenutni_cvor.daj_decu():
                #ako imamo onda dodamo poziciju i prelazimo na sledece
                ima_cvor = trenutni_cvor.daj_cvor(rec[index])
                ima_cvor.dodaj_poziciju(pozicija, kraj)
                trenutni_cvor = ima_cvor
            else:
                #ako nemamo ovo slovo napravimo ga i prelazimo na sledece
                novi_cvor = self.Cvor(rec[index], index)
                novi_cvor.dodaj_poziciju(pozicija, kraj)
                trenutni_cvor.dodaj_dete(novi_cvor)
                trenutni_cvor = novi_cvor

    def daj_pozicije_reci(self, rec):
        rec = rec.lower()
        trenutni_cvor = self._koren
        for i in range(len(rec)):
            if i != len(rec) - 1:
                if rec[i] in trenutni_cvor.daj_decu():
                    trenutni_cvor = trenutni_cvor.daj_cvor(rec[i])
                else:
                    return []
            else:
                if rec[i] in trenutni_cvor.daj_decu():
                    trenutni_cvor = trenutni_cvor.daj_cvor(rec[i])
                    pozicije = trenutni_cvor.daj_pozicije()
                    return [el[0] for el in pozicije if el[1] == True]
                else:
                    return []
