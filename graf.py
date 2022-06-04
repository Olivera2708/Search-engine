class Graf:
  class Cvor:
    def __init__(self, putanja, reci):
      self._putanja = putanja
      self._reci = reci
  
    def putanja(self):
      return self._putanja

    def __str__(self):
      return f"{self._putanja}"
    
  class Ivica:
    def __init__(self, izvor, destinacija):
      self._izvor = izvor
      self._destinacija = destinacija
  
    def krajevi(self):
      return (self._izvor, self._destinacija)
  
    def suprotno(self, v):
      if not isinstance(v, Graf.Cvor):
        raise TypeError('v mora biti instanca klase Cvor')
      if self._destinacija == v:
        return self._izvor
      elif self._izvor == v:
        return self._destinacija
      raise ValueError('v nije cvor ivice')

    def __str__(self):
      return '({0}, {1})'.format(self._izvor, self._destinacija)
    

  def __init__(self):
    self._izlaze = {}
    self._dolaze = {}

  def _jel_postoji_cvor(self, v):
    if not isinstance(v, self.Vertex):
      raise TypeError('Ocekivan je objekat klase Vertex')
    if v not in self._izlaze:
      raise ValueError('Vertex ne pripada ovom grafu.')

  def broj_cvorova(self):
    return len(self._izlaze)

  def cvorovi(self):
    return self._izlaze.keys()

  def broj_ivica(self):
    total = sum(len(self._izlaze[v]) for v in self._izlaze)
    return total

  def ivice(self):
    result = set()
    for secondary_map in self._izlaze.values():
      result.update(secondary_map.values())
    return result

  def daj_ivicu(self, u, v):
    self.jel_postoji_cvor(u)
    self.jel_postoji_cvor(v)
    return self._izlaze[u].get(v)

  def daj_cvor(self, link):
    for cvor in self.cvorovi():
      if link in cvor.putanja():
        return cvor

  def degree(self, v):
    self._validate_vertex(v)
    adj = self._izlaze
    return len(adj[v])

  def vezane_ivice(self, v):   
    self._validate_vertex(v)
    adj = self._izlaze
    for edge in adj[v].values():
      yield edge

  def dodaj_cvor(self, putanja, reci):
    v = self.Cvor(putanja, reci)
    self._izlaze[v] = {}
    self._dolaze[v] = {}
    return v
      
  def dodaj_ivicu(self, u, v):
    e = self.Ivica(u, v)
    self._izlaze[u][v] = e
    self._dolaze[v][u] = e
