# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 07:58:36 2016

@author: pawel
"""
#for a in range(1,46):
 #   print(a)
print("WITAJ W LOTEK ;)\n")
op = "s"
while op == "s":
   op = input("Wygenerować liczby(t/n)? ")

while op== "t":
    licznik=0
    while True:
        from random import randint
        print("random number ",randint(1,49))
        licznik += 1
        if licznik >= 6:
            op = input("Jeszcze raz(t/n)? ")
            break


    print


while op == "n":
    import time
    time.sleep(3)
    print("Good Luck")
    time.sleep(3)
    
    op="s"

    
    

#for a in range(1,46):
 #   print(a)
