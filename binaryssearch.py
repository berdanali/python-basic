# Binary Search python kodlaması .... 


def binarySearch(sayı, x, low, high):

    
    while low <= high:

        orta = low + (high - low)//2

        if sayı[orta] == x:
            return orta

        elif sayı[orta] < x:
            low = orta + 1

        else:
            high = orta - 1

    return -1


sayı = [3, 4, 5, 6, 7, 8, 9]
x = 6

result = binarySearch(sayı, x, 0, len(sayı)-1)

if result != -1:
    print("Sayının bulunduğu yer :  " + str(result))
else:
    print("Sayı Dizide bulunamadı ... ")

