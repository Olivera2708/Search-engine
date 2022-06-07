from hashmap import LinearHashMap

class Trie:
    class Cvor:
        def __init__(self, karakter = "", dubina = 0):
            self._karakter = karakter
            #cuvam pozicije [pozicija, vrednost] - vrednost je True ili False, da li je kraj reci
            self._pozicije = []
            #cuvam kljuc karakter, vrednost cvor
            if dubina == -1:
                self._deca = LinearHashMap(52) #najbolje 52
            elif dubina == 0:
                self._deca = LinearHashMap(26) #najbolje 26
            elif dubina == 1:
                self._deca = LinearHashMap(16) #najbolje 16
            else:
                self._deca = LinearHashMap(4) #najbolje 4

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
        self._koren = self.Cvor("", -1)
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
        duzina_reci = len(rec)
        for index, slovo in enumerate(rec):
            kraj = False
            if index == duzina_reci-1:
                kraj = True
            try:
                #ako imamo onda dodamo poziciju i prelazimo na sledece
                ima_cvor = trenutni_cvor.daj_cvor(slovo)
                ima_cvor.dodaj_poziciju(pozicija, kraj)
                trenutni_cvor = ima_cvor
            except:
                #ako nemamo ovo slovo napravimo ga i prelazimo na sledece
                novi_cvor = self.Cvor(slovo, index)
                novi_cvor.dodaj_poziciju(pozicija, kraj)
                trenutni_cvor.dodaj_dete(novi_cvor)
                trenutni_cvor = novi_cvor

    def daj_pozicije_reci(self, rec):
        rec = rec.lower()
        trenutni_cvor = self._koren
        duzina_reci = len(rec)
        for i, slovo in enumerate(rec):
            if i != duzina_reci - 1:
                try:
                    trenutni_cvor = trenutni_cvor.daj_cvor(slovo)
                except:
                    return []
            else:
                try:
                    trenutni_cvor = trenutni_cvor.daj_cvor(slovo)
                    pozicije = trenutni_cvor.daj_pozicije()
                    return [el[0] for el in pozicije if el[1] == True]
                except:
                    return []