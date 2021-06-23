# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:50:00 2016

@author: pawel
"""
op = "t"
while op == "t":
    depth = 0
    #CN=[720,570,450,360,300,240,210,180,150,120,45]
    cnsTable = {0.6:720, 0.7:570, 0.8:450,0.9:360,1.0:300,1.1:240,1.2:210,1.3:180,1.4:150,1.5:120,1.6:45}
    NDLtime = 30
    NDLair = 20
    
    Nx = input('Podaj rodzaj gazu:')
    
    
    if Nx in range(30,33):
        print"Gratulacje, wybrałeś nitrox", Nx
        depth = input('Podaj swoją głębokość:')
        
        if depth == 30:
            NDLtime = 30
        elif depth in range(31,34):
            NDLtime = 25
        elif depth in range(34,37):
            NDLtime = 20
        elif depth in range(37,40):
            NDLtime = 15
        elif depth in range(41,201):
            print"Minimum deco is not suitable for dives 40meters over,"
            print"also your PPO2 is to high!"
            check = input("Jeszcze raz (t/n)? ")
        elif depth in range(27,30):
            NDLtime = 35
        elif depth in range(24,27):
            NDLtime = 40
        elif depth in range(21,24):
            NDLtime = 45
        elif depth in range(18,21):
            NDLtime = 50
        elif depth in range(15,18):
            NDLtime = 55
        elif depth in range(0,15):
            print"You are shallow, possibly gas in your single cylinder"
            print"will finish earlier than you hit your decompression obligations!"
            op = raw_input("Jeszcze raz (t/n)? ")
        elif depth > 200:
            print"Are you sick? Better stop dive today ;)"
            op = raw_input("Jeszcze raz (t/n)? ")

        time = input('Podaj czas denny - Bottom Time:')
    

        # GUE Formulas based calculations
        print"GUE Formulas"

        # EAD - Equivalent Air Depth calculations
        print"Your Equivalent Air Depth for Nx is", depth*0.8, "m"
    
        # PPO2 calculations
        ppo2 = (Nx*0.01)*(depth*0.1+1)
        a = round(ppo2,1)
        print"Your higgest PPO2 for",depth,"m dive is",ppo2
        
        # CNS calculations
        b=a*10
        if b in range(6,17):
            singleExp = cnsTable[a]
            #print"Single max exposure for that dive is",singleExp,"min"
        elif b in range(0,6):
            singleExp=1
            print "to shallow"
        elif b in range(17,200):
            singleExp=0
            print "to deep"

        # CNS formula
        cns = (time*1.00)/(1.0*singleExp)*100
        roundCns = round(cns,1)  
        print"Your CNS is ",roundCns,"%"
            
        # OTU calculations
        otu = time*1.5
        print"Your OTU is", otu
           
        print"Your NDL is", NDLtime,"minutes"
        
        op = raw_input("Jeszcze raz (t/n)? ")
            
    elif Nx == 21:
        print"Wybrałeś Air"
        op = raw_input("Jeszcze raz (t/n)? ")
    elif Nx < 21 and Nx > 0:
        print"Your gas is hypooxic, rise your PPO2 fraction"
        op = raw_input("Jeszcze raz (t/n)? ")
    else :
        print"Gaz który wybrałeś nie jest rekomendowany i obsługiwany przez nasz kalkulator"
        op = raw_input("Jeszcze raz (t/n)? ")
    

    
    #op = raw_input("Jeszcze raz (t/n)? "
z = 0

while z == 0:
    import time
    print "Dive safe"
    time.sleep(3)
    z += 1
