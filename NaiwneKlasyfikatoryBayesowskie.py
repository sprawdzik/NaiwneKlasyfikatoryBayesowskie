#Skrypt obliczając współczynnik prawdopodobieństwa zatrudnienia nowego pracownika w opraciu o oferowane benefity w ogłoszeniu
#https://pl.wikipedia.org/wiki/Naiwny_klasyfikator_bayesowski

#import danych z pliku txt
ogloszenie = open("ogloszenia.txt", "r")
li2  = list([line.rstrip('\n') for line in ogloszenie])

#zmienne
dane=[] 
tak={}
nie={}
prawdTak = prawdNie = wspolczynnik =1 #prawdopodobienstwo na tak i nie oraz wspolczynnik normalizacji 
#(ilosc slow na tak, ilosc na nie podzielone przez wszystkie slowa z kazdej kategorii, np. pilkarzyki tak + pilkarzyki nie / wszystkie slowa)

#Dane do testu
# daleko - dojazd do pracy zajmuje powyżej 30 min
# lunch - firma zapewnia darmowy lunch
# multisport - firma zapewnia kartę do siłowni
# napoje - firma zapewnia darmowe napoje
# owoce - firma zapewnia owocowy dzień
# parking - firma oferuje darmowy parking samochodowy
# pilkarzyki - w firmie są piłkarzyki w strefie chill
# rower - dofinansowanie za dojazdy rowerem
# stacjonarnie - brak możliwości pracy zdalnej
# wyplata10k - wypłata >= 10 000 PLN netto
# wyplata3k - wypłata <= 3 000 PLN netto
# xbox - w firmie jest xbox w strefie chill
# zdalnie - możliwość zdalnej pracy

#zadanie testu
test=['zdalnie','pilkarzyki','wyplata10k']
#test=['zdalnie','pilkarzyki']
#test=['zdalnie','multisport']

#kategoria
i=0
for linia in li2:
    #przygotowanie danych do kategoryzacji
    dane=li2[i].split(' ')
    kategoria=(dane.pop(0))
    #kategoryzacja danych TAK / NIE
    for slowo in dane:
        if kategoria == 'TAK':
            if slowo in tak.keys():
                tak[slowo] = tak[slowo] +1
            else:
                tak[slowo] = 1
        else:
            if slowo in nie.keys():
                nie[slowo] = nie[slowo] +1
            else:
                nie[slowo] = 1
    i+=1  

#wyświetlnie podsumowania danych w kategoriach 
#print("Tak: ",tak)
#print("Nie: ",nie)

#prawdopodobieństwo wg. Bayesa
for s1 in test:
    #sprawdzam czy benefit występuje w słowniku na tak
    if s1 not in tak.keys():
        tak[s1] = 0
    prawdTak *= (tak[s1] + 1) / sum(tak.values()) # 1 żeby nie było 0   
    #sprawdzam czy benefit występuje w słowniku na nie
    if s1 not in nie.keys():
        nie[s1] = 0
    prawdNie *= (nie[s1] + 1) / sum(nie.values()) # 1 żeby nie było 0
    #obliczenie współczynnika
    wspolczynnik *= (tak[s1] + nie[s1]) / (sum(tak.values()) + sum(nie.values())) 

prawdTak *= len(tak) / (len(tak) + len(nie))
prawdNie *= len(nie) / (len(tak) + len(nie))

# wyliczenie wspolczynnika prawdopodobienstwa
print("Współczynnik zatrudnienia osoby w oparciu o benefity: ", test)
wspolczynnikTak=prawdTak/wspolczynnik
wspolczynnikNie=prawdNie/wspolczynnik
print("Tak: ",wspolczynnikTak)
print("Nie: ",wspolczynnikNie)
if wspolczynnikTak>wspolczynnikNie:
    print("Tak do nie: ",wspolczynnikTak/wspolczynnikNie)
else:
    print("Nie do tak: ",wspolczynnikNie/wspolczynnikTak)