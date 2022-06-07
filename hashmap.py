import random
from map import MapElement

class HashMap(object):
    def __init__(self, capacity=800):
        self._data = capacity * [None]
        self._capacity = capacity
        self._size = 0
        self.prime = 109345121

        # konstante heširanja
        self._a = 1 + random.randrange(self.prime-1)
        self._b = random.randrange(self.prime)

    def __len__(self):
        return self._size

    def _hash(self, x):
        if isinstance(x, str):
            return ord(x) % self._capacity
        hashed_value = (hash(x)*self._a + self._b) % self.prime
        return hashed_value % self._capacity

    def _resize(self, capacity):
        old_data = list(self.items())
        self._data = capacity * [None]
        self._size = 0

        # prepisivanje podataka u novu tabelu
        for (k, v) in old_data:
            self[k] = v

    def __getitem__(self, key):
        bucket_index = self._hash(key)
        return self._bucket_getitem(bucket_index, key)

    def __setitem__(self, key, value):
        bucket_index = self._hash(key)
        self._bucket_setitem(bucket_index, key, value)

        # povećaj broj raspoloživih mesta
        current_capacity = len(self._data)
        if self._size > current_capacity * 0.75:
            self._resize(2*current_capacity - 1)

class LinearHashMap(HashMap):
    # sentinel koji označava lokaciju u mapi sa koje je obrisan element
    _MARKER = object()

    def _is_available(self, bucket_index):
        return self._data[bucket_index] is None or self._data[bucket_index] is self._MARKER

    def _find_bucket(self, bucket_index, key):
        available_slot = None
        while True:
            if self._is_available(bucket_index):
                if available_slot is None:
                    available_slot = bucket_index

                if self._data[bucket_index] is None:
                    return False, available_slot

            elif key == self._data[bucket_index].key:
                return True, bucket_index

            bucket_index = (bucket_index+1) % len(self._data)

    def _bucket_getitem(self, bucket_index, key):
        found, index = self._find_bucket(bucket_index, key)
        if not found:
            raise KeyError('Ne postoji element sa traženim ključem.')
        return self._data[index].value

    def _bucket_setitem(self, bucket_index, key, value):
        found, available_bucket_index = self._find_bucket(bucket_index, key)
        if not found:
            self._data[available_bucket_index] = MapElement(key, value)
            self._size += 1
        else:
            self._data[available_bucket_index].value = value

    def __iter__(self):
        for i in range(len(self._data)):
            if not self._is_available(i):
                yield self._data[i].key

    def items(self):
        for i in range(len(self._data)):
            if not self._is_available(i):
                yield self._data[i].key, self._data[i].value

    def keys(self):
        lista = []
        for i in range(len(self._data)):
            if not self._is_available(i):
                lista.append(self._data[i].key)
        return lista

    def values(self):
        lista = []
        for i in range(len(self._data)):
            if not self._is_available(i):
                lista.append(self._data[i].value)
        return lista
