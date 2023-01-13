import random
ben=0
sen=0


while ben!=3 or sen!=3:
 secenekler = int(input("Taş: 0, Kağıt: 1, Makas: 2 :"))
 kısı2 = random.randint(0,2)
 kısı1=secenekler
    
 if(kısı1 == kısı2):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("Berabere ... ")
    print("Skor Tablosu : ", ben , sen)
 elif(kısı1 ==0 and kısı2 == 1):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("kaybettiniz ... ")
    sen+=1
    print("Skor Tablosu : ", ben , sen)

 elif(kısı1 == 0 and kısı2 == 2):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("Ben kazandım ... ")   
    ben+=1
    print("Skor Tablosu : ", ben , sen)

 elif(kısı1 == 1 and kısı2 == 0):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("Ben kazandım ... ")  
    ben+=1
    print("Skor Tablosu : ", ben , sen)

 elif(kısı1 == 1 and kısı2 == 2 ):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("Kaybettiniz ... ")   
    sen+=1 
    print("Skor Tablosu : ", ben , sen)

 elif(kısı1 == 2 and kısı2 == 0):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("Kaybettiniz ... ")   
    sen+=1
    print("Skor Tablosu : ", ben , sen)

 elif(kısı1 ==2 and kısı2 == 1):
    print("BİLGİSAYARIN SEÇİMİ : " , kısı2)
    print("Ben kazandım ... ")   
    ben+=1
    print("Skor Tablosu : ", ben , sen)

 
