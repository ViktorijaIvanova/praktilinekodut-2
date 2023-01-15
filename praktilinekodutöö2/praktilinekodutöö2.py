from math import*
from random import*
#harjutus 8
int(input)
random_number = random.randint(1,100)
print(random_number)
a = 1
a+=1
if a % 2 == 0:
    print("paarisarv")
else:
    print("paaritu number")
while a < 101:
    print("tsükkel on lõpp")

    







#harjutus 0.2
x=int()
s=0
viimane=0
pr=1
maksimaalselt=3
miinimum=0
while True:
    if x>0:
      viimane=x%10
      miinimum=miinimum+1
    if viimane%2==0:
        maksimaalselt+=1
    s=s+viimane
    pr=pr*viimane 
    if viimane>maksimaalselt:
        maksimaalselt=viimane 
    if viimane>miinimum:
        miinimum=viimane 
    x=x//10
    print("sööge minimaalne arv kordi",miinimum)
    print ("sööge maksimaalselt arv kordi",maksimaalselt)
    print ("kõigi aegade summa",s)
    print ("kõigi aegade  korrutama",pr)
    break

#harjutus 0
x=int()
s=0
pr=1
maksimaalselt=3
miinimum=0
while x>0:
    viimane=x%10
    miinimum=miinimum+1
    if viimane%2==0:
        maksimaalselt+=1
    s=s+viimane
    pr=pr*viimane 
    if viimane>maksimaalselt:
        maksimaalselt=viimane 
    if viimane>miinimum:
        miinimum=viimane 
    x=x//10
print("sööge minimaalne arv kordi",miinimum)
print ("sööge maksimaalselt arv kordi",maksimaalselt)
print ("kõigi aegade summa",s)
print ("kõigi aegade  korrutama",pr)

#harjutus 8.2
a=1
while True:
    print(a)
    if a >= 100:
       break
    a+=1

#ülesanne 6
n=0
print ("*kolmnurga")
for e in range (11,0,-1):
    n = n+1
    for f in range (0, n+1):
        print ("*", end = "")
    print()
print("")



Exercise 8.1
a = random.randint(1, 100)
a = int(input("sisetaga number:"))

while a < 101:
    
    if a % 2 == 0:
        print("paaris number")
        print("tsükkel on lõpp")
    elif a % 2 == 1:
        print("paaritu number")
        print("tsükkel on lõpp")
    break

else:
    print("Proovige veel üks kord")
    
    
    
Exercise 8.2
from math import*

a = int(input("sisetage number:"))

while True:
        if a <= 100:
            print(a)
            if a % 2 == 0:
                print("paaris number")
                print("tsükkel on lõpp")
            elif a % 2 == 1:
                print("paaritu number")
                print("tsükkel on lõpp")
            break
        
        else:
            print("Proovige veel kord")
            break
            
            
         

Exercise 0.1
indeks=int(input("Kirjuta oma postindeksi: "))#12345
a=5

while len(str(indeks)) == a:
    print("See on sinu postindeks")
    print(indeks)#12345
    break
else:
    print('Ebakorrektne indeks, indeksil on peab olema 5 tähti')
    


Exercise 0.2
while True:
    try:
        indeks = input("Kirjuta oma postindeksi: ")#12345
        if (5 == len(indeks) and indeks.isdigit()):
            break
        else:
            print('Ebakorrektne indeks, indeksil on peab olema 5 tähti')
    except :
        print("Viga")
print("See on sinu postindeks")
print(indeks)#12345















