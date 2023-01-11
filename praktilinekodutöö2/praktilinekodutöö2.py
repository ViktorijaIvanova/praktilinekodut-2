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














