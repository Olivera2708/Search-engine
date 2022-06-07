###Strukture

##Graf (usmeren)
Sastoji se od cvora i grana.
U cvoru cuvam putanju do fajla (html stranice), reci na stranici, kao i strukturu Trie koja je nastala od datih reci.
Grane sluze kako bih povezala cvorove medjusobno.

##Trie
Sastoji se od cvorova.
Svaki cvor ima karakter, decu i pozicije (na kom mestu u listi reci se nalazi ovo slovo u ovom cvoru).
#Ucitavanje u Trie:
Za svaku rec idem slovo po slovo, gledam da li postoji vec cvor sa tim slovom, ako postoji cuvam poziciju i idem dalje, ako je postoji pravim cvor sa tim slovom, povezujem ga sa cvorom iznad i cuvam poziciju.
#Citanje iz trie:
Za svaku rec idem po slovima, ako naidjem da nema cvora koji ima slovo na redu, onda se rec ne nalazi na zadatoj strani, ako dodjem do poslednjeg slova, proverim i jel njega ima, ako ima onda vracam pozicije svih pojavljivanja date reci.

##Sortiranje
Koriscen je merge sort, prilagodjen za listu listi.

