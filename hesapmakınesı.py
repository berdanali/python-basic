
def topla(sayı1, sayı2):
    return sayı1+sayı2


def cıkar(sayı1, sayı2):
    return sayı1-sayı2


def carp(sayı1, sayı2):
    return sayı1*sayı2


def bolme(sayı1, sayı2):
    return sayı1/sayı2


print("Hosgeldınız...")
print("1  toplama")
print("2  cıkarma")
print("3  carpma")
print("4  bolme")

sayı1 = input("sayı1 ı gır  ... ")
sayı2 = input("sayı2 ı gır ... ")
secım = int(input("secımı gırınız : "))

if (secım == 1):
    print(topla(int(sayı1), int(sayı2)))
    
elif (secım == 2):
    print(cıkar(int(sayı1), int(sayı2)))

elif (secım == 3):
    print(carp(int(sayı1), int(sayı2)))

elif (secım == 4):
    print(bolme(int(sayı1) , int(sayı2)))

else:
    print("Lütfen beriltilen degerlerden bırını gırınız ")    