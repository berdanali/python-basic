import random

MAX_SATIR = 3
MAX_BAHİS = 1000
MİN_BAHİS = 1

ROWS = 3
COLS = 3

kelime_sayıcı = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
kelime_vaule = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def kazandımı(sutunlar , satırlar , bahis, vaule ):
    kazanc = 0
    kazanc_satırı = []
    for satır in range (satırlar):
        kelime = sutunlar[0][satır]
        for sutun in sutunlar:
            kelime_to_check =  sutun[satır]
            if kelime != kelime_to_check:
                break   
        else:
            kazanc +=vaule[kelime] * bahis
            kazanc_satırı.append(satır + 1)

    return kazanc , kazanc_satırı

def slot_makinsei_spin(rows, cols, kelimeler):
    tum_kelimeler = []
    for kelime, kelime_sayıcı in kelimeler.items():
        for _ in range(kelime_sayıcı):
            tum_kelimeler.append(kelime)
    sutunlar = []
    for _ in range(cols):
        sutun = []
        gecerli_kelimeler = tum_kelimeler[:]
        for _ in range(rows):
            vaule = random.choice(gecerli_kelimeler)
            gecerli_kelimeler.remove(vaule)
            sutun.append(vaule)
        sutunlar.append(sutun)

    return sutunlar

   # [A, A, C]
   # [A, A, A]
   # [B, A, A]


def print_slot_makine(sutunlar):
    for row in range(len(sutunlar[0])):
        for i, sutun in enumerate(sutunlar):
            if i != len(sutunlar) - 1:
                print(sutun[row], end= " | ")
            else:
                print(sutun[row], end = " ")
        print()

def deposito():
    while True:
        miktar = input("Ne kadar para yatırcaksınız ?  $")
        if miktar.isdigit():
            miktar = int(miktar)
            if miktar > 0:
                break
            else:
                print("Girilen miktar 0'dan küçük olamaz! ")
        else:
            print("Lütfen bir sayı giriniz ... ")

    return miktar


def bahis_al():
    while True:
        miktar = input("Ne kadar bahis girmek istersin ?  $")
        if miktar.isdigit():
            miktar = int(miktar)
            if MİN_BAHİS <= miktar <= MAX_BAHİS:
                break
            else:
                print(
                    f"Lütfen aralıkta bir değer giriniz! ${MİN_BAHİS} - ${MAX_BAHİS} ")
        else:
            print("Lütfen bir sayı giriniz ... ")

    return miktar


# 100 yatırdı dıyelım 3 satır oynamak istiyorsa kazanırsa 300 alacak
def satır_sayısı():
    while True:
        satır = input(
            "Bahis yapılacak satır sayısını giriniz (1-" + str(MAX_SATIR) + ")? ")
        if satır.isdigit():
            satır = int(satır)
            if 1 <= satır <= MAX_SATIR:
                break
            else:
                print("Geçerli bir numara giriniz ")

        else:
            print("Lütfen bir sayı giriniz ... ")

    return satır

def spin(balance):
    satırlar = satır_sayısı()
    while True:
        bahis = bahis_al()
        toplam_bahis = bahis * satırlar

        if toplam_bahis > balance:
            print(
                f"Bu miktarda girmek için yeterli bakiyeniz yok Olan bakiyeniz : ${balance}")
        else:
            break

    print(
        f"Bahistesin ${bahis} on {satırlar} satırında. Toplam bahisin : ${toplam_bahis}")

    slots = slot_makinsei_spin(ROWS, COLS, kelime_sayıcı)
    print_slot_makine(slots)
    kazanc, kazanc_satırı = kazandımı(slots, satırlar, bahis, kelime_vaule)
    print(f"Kazandın ${kazanc}.")
    print(f"Satırda kazandın:", *kazanc_satırı)
    return kazanc - toplam_bahis



def main():
    balance = deposito()
    while True:
        print(f"Geçerli bakiyeniz :  ${balance}")
        answer = input("Oynamak için entere basın (q çıkış).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"İle ayrıldın ${balance}")
main()
