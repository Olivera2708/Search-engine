from hashmap import LinearHashMap
from trie import Trie

class Graf:
  class Cvor:
    def __init__(self, putanja, reci):
      self._putanja = putanja
      self._reci = reci
      self._trie = Trie(reci)

    def daj_trie(self):
      return self._trie

    def daj_pozicije(self):
      return self._pozicije

    def daj_reci(self):
      return self._reci
  
    def daj_putanju(self):
      return self._putanja
    
  class Grana:
    def __init__(self, izvor, destinacija):
      self._izvor = izvor
      self._destinacija = destinacija
  
    def krajevi(self):
      return (self._izvor, self._destinacija)
  
    def suprotno(self, v):
      if not isinstance(v, Graf.Cvor):
        raise TypeError('Nije instanca klase Cvor')
      if self._destinacija == v:
        return self._izvor
      elif self._izvor == v:
        return self._destinacija
      raise ValueError('Nije cvor grane')

    def __str__(self):
      return '({0}, {1})'.format(self._izvor, self._destinacija)
    
  def __init__(self):
    self._izlaze = LinearHashMap()
    self._dolaze = LinearHashMap()

  def _jel_postoji_cvor(self, v):
    if not isinstance(v, self.Cvor):
      raise TypeError('Ocekivan je objekat klase Cvor')
    if v not in self._izlaze:
      return False
    return True

  def broj_cvorova(self):
    return len(self._izlaze)

  def cvorovi(self):
    return self._izlaze.keys()

  def broj_grana(self):
    #za svaki cvor broji koliko grana izlazi iz njega
    return sum(len(self._izlaze[v]) for v in self._izlaze)

  def grane(self):
    return self._izlaze.values()

  def daj_cvor(self, link):
    for cvor in self.cvorovi():
      if link == cvor.daj_putanju():
        return cvor

  def broj_grana_dolaze(self, v):
    return len(self._dolaze[v])

  def grane_dolaze(self, v):
    return list(self._dolaze[v].keys())

  def dodaj_cvor(self, putanja, reci):
    v = self.Cvor(putanja, reci)
    self._izlaze[v] = LinearHashMap(80)
    self._dolaze[v] = LinearHashMap(80)
    return v
      
  def dodaj_granu(self, u, v):
    e = self.Grana(u, v)
    self._izlaze[u][v] = e
    self._dolaze[v][u] = e
