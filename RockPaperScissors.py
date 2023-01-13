import random
ben = 0
sen = 0
while 1 == 1:
    secenekler = int(input("Taş: 0, Kağıt: 1, Makas: 2 :"))
    kısı2 = random.randint(0, 2)
    kısı1 = secenekler

    if (kısı1 == kısı2):
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "Berabere ... ", '\n', "Skor Tablosu : ", ben, sen)

    elif (kısı1 == 0 and kısı2 == 1):
        sen += 1
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "kaybettiniz ...", '\n', "Skor Tablosu : ", ben, sen)

    elif (kısı1 == 0 and kısı2 == 2):
        ben += 1
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "Ben kazandım ... ", '\n', "Skor Tablosu : ", ben, sen)

    elif (kısı1 == 1 and kısı2 == 0):
        ben += 1
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "Ben kazandım ... ", '\n', "Skor Tablosu : ", ben, sen)

    elif (kısı1 == 1 and kısı2 == 2):
        sen += 1
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "kaybettiniz ...", '\n', "Skor Tablosu : ", ben, sen)

    elif (kısı1 == 2 and kısı2 == 0):
        sen += 1
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "kaybettiniz ...", '\n', "Skor Tablosu : ", ben, sen)

    elif (kısı1 == 2 and kısı2 == 1):
        ben += 1
        print("BİLGİSAYARIN SEÇİMİ : ", kısı2, '\n',
              "Ben kazandım ... ", '\n', "Skor Tablosu : ", ben, sen)

    if (ben == 3 or sen == 3):
        break
if (ben == 3):
    print("Ben kazandım .. ")
else:
    print("Sen kazandın ")
