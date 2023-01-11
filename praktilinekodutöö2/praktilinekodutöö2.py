from math import*
from random import*
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

#harjutus 8
a = 1
while a < 101:
    print("Tsükkel lõpetatud", a, "aeg(a)")
    a = a+1
print("tsükkel on lõpp")
