# Opis

## Graf (usmeren)
Sastoji se od cvora i grana.
U cvoru cuvam putanju do fajla (html stranice), reci na stranici, kao i strukturu Trie koja je nastala od datih reci.
Grane sluze kako bih povezala cvorove medjusobno (preko linkova).

## Trie
Sastoji se od cvorova.
Svaki cvor ima karakter, decu i pozicije (na kom mestu u listi reci se nalazi ova rec).
Upisivanje:
Za svaku rec idem slovo po slovo, gledam da li postoji vec cvor sa tim slovom, ako postoji cuvam poziciju i idem dalje, ako je postoji pravim cvor sa tim slovom, povezujem ga sa cvorom iznad i cuvam poziciju.
Citanje:
Za svaku rec idem po slovima, ako naidjem da nema cvora koji ima slovo na redu, onda se rec ne nalazi na zadatoj strani, ako dodjem do poslednjeg slova, proverim jel njega ima, ako ima onda vracam pozicije svih pojavljivanja date reci.

## Hesmapa
Ako je kljuc karakter, onda hes funkciju pravim uz pomoc ascii vrednosti karaktera. 
Inace koristim hes funkciju sa vezbi. 

## Sortiranje
Koriscen je merge sort, prilagodjen za listu listi.

## Pretraga
1. Rec
Za unesenu rec uzmem broj pojavljivanja reci u dokumentu, broj linkovanja na dokument, kao i broj pojavljivanja reci u dokumentu koji ga linkuje, poslednji broj delim sa 8.
Sabiranjem tri dobijena broja dobijam rang.

2. Reci odvojene razmakom
Za svaku rec izracunam rang, kao u 1. i podelim sa brojem reci. 
Na taj nacin dobijam rang. 

3. Operator NOT
Za prvu rec proverim da li je ima u fajlu, ako nema preskacem ga. Ako ima provaravam da li druge reci ima u fajlu, ako ima preskacem, ako nema racunam rang kao u 1. slucaju. 

4. Operator AND
Proveravam da li su obe reci u fajlu, ako jesu racunam rang obe reci odvojeno i rezultate saberem i podelim sa 2.

5. Operator OR
Slicno kao 2. samo se rang racuna na osnovu reci koje ima vise u fajlu.

# Dodatni zadatak (pretraga izraza)
Za svaku rec vrati pozicije pojavljivanja. 
Proveravam rekurzivno da li postoji neki broj u poziciji prve reci, tako da se broj+1 nalazi u poziciji druge reci, pa analogno za ostale reci. 
