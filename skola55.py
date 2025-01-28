kroky = [13443,8832,3450,7765,14098]
cvicenia = ["beh","X","plavanie","beh","fitko"]
kalorie = [810,400,590,790,840]

def pridaj_den(kr,cv,kcal):
    kroky.append(kr)
    cvicenia.append(cv)
    kalorie.append(kcal)
    print("Uspesne ste pridali den")
    print("-",kr,"krokov")
    print("-",cv)
    print("-",kcal,"Kalorii")

def posldnych_5():
    print("vypisujem poslednych 5dni")
    for i in range(len(kroky),len(kroky)-6,-1):
        print("---",i+1,"den")
        print(i)