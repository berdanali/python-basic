import random
def number_guest(tahmin):
    sayı = random.randint(1, 1000)
    while 1 == 1:
        tahmin = int(
            input(print("Lütfen tahmin yapın , tekte bilirsen zurna benden :)")))
        print("********************************************************")

        if (sayı == tahmin):
            print("Doğru tahmin zurna kac cm olsun ")
            break

        elif (sayı < tahmin):
            print("Sayıyı küçült ... ")
            print("********************************************************")

        else:
            print("Sayıyı büyüt ... ")
            print("********************************************************")


number_guest(1)
