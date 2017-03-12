""" Palindromik Asal Sayılar """
import time

starttime= time.time()
def asal(sayi):
    x=int(sayi)
    i=2
    while (x>i):
        dogru=0
        if (x%i==0):
            break
        else:
            dogru=1
        i+=1

    return dogru

def main():
    deger=3
    while (deger<100000):
        if (asal(deger)==1):
            deger=str(deger)
            if (len (deger)==1):
                print (deger)
            elif (len (deger)==2 and deger [0] == deger [-1]):
                print(deger)
            elif (len (deger)==3 and deger [0] == deger [-1]):
                print(deger)
            elif (len (deger)==4 and deger [0] == deger [-1] and deger [1] == deger [-2]):
                print(deger)
            elif (len (deger)==5 and deger [0] == deger [-1] and deger [1] == deger [-2]):
                print(deger)
            elif (len (deger)==6 and deger [0] == deger [-1] and deger [1] == deger [-2] and deger [2] == deger [-3]):
                print(deger)
            deger =int(deger)
        deger+=1
main()

starttime2= time.time()

print(starttime2-starttime)
