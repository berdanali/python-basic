import random
oyuncuBirİcin = True
oyuncuİkiİcin = True
# deste      oyuncu1 oyuncu2
deste = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4
oyuncuBir = []
oyuncuİki = []


def kartHesapla(donus):
    card = random.choice(deste)
    donus.append(card)
    deste.remove(card)


def total(donus):
    total = 0
    yuz = ('Q', 'J', 'K')

    for card in donus:
        if card in range(1, 11):
            total += card
        elif card in yuz:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


def oyuncununEli():
    if len(oyuncuİki) == 2:
        return oyuncuİki[0]
    elif len(oyuncuİki) > 2:
        return oyuncuİki[0], oyuncuİki[1]


for _ in range(2):
    kartHesapla(oyuncuİki)
    kartHesapla(oyuncuBir)

while oyuncuBirİcin or oyuncuİkiİcin:
    print(f"oyuncu ikide {oyuncununEli()} and X")
    print(f"seninkiler{oyuncuBir}toplam {total(oyuncuBir)}")
    if oyuncuBirİcin:
        kalyadaCek = int(input("1:kal\n2:cek\n"))
    if total(oyuncuİki) > 16:
        oyuncuİkiİcin = False
    elif total(oyuncuİki) < 17:
        kartHesapla(oyuncuBir)
    if kalyadaCek == 1:
        oyuncuBirİcin = False
    elif kalyadaCek == 2:
        kartHesapla(oyuncuBir)
    if total(oyuncuBir) >= 21:
        break
    elif total(oyuncuİki) >= 21:
        break


if total(oyuncuBir) == 21:

    print(f"sen{oyuncuBir}toplam{total(oyuncuBir )}  karta sahipsin ve {(oyuncuİki)} {total(oyuncuİki)} karta sahip")

    print("blackJack oyuncu 1  kazandı")

elif total(oyuncuİki) == 21:

    print(f"sen{oyuncuİki}toplam{total(oyuncuBir )} sahipsin ve {(oyuncuİki)} {total(oyuncuİki)} sahip")

    print("blackJack oyuncu 2 kazandın")

elif total(oyuncuBir) > 21:

    print(f"sen{oyuncuBir}toplam{total(oyuncuBir )} sahipsin ve {(oyuncuİki)} {total(oyuncuİki)} sahip")

    print("iflas oyuncu 1 ettin oyuncu iki kazandı ")

elif total(oyuncuİki) > 21:

    print(f"sen{oyuncuBir}toplam{total(oyuncuBir )} sahipsin ve {(oyuncuİki)} {total(oyuncuİki)} sahip")

    print("iflas ettin oyuncu 2 oyuncu 1 kazandı")


elif 21-total(oyuncuİki) < 21-total(oyuncuBir):

    print(f"sen{oyuncuBir}toplam{total(oyuncuBir )} sahipsin ve {(oyuncuİki)} {total(oyuncuİki)} sahip")

    print("oyuncu iki kazandı")


elif 21-total(oyuncuİki) > 21-total(oyuncuBir):

    print(f"sen{oyuncuBir}toplam{total(oyuncuBir )} sahipsin ve {(oyuncuİki)} {total(oyuncuİki)} sahip")

    print("oyuncu bir kazandı")
