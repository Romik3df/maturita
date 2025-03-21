
import random
import getpass

#chat gpt
def registracia():
    user_name = input("Zadaj svoje meno: ")
    pass1 = getpass.getpass("Zadaj heslo: ")  # Heslo sa nezobrazuje
    pass2 = getpass.getpass("Zadaj heslo znova: ")

    if pass1 == pass2:
        print("Ste úspešne zaregistrovaný")
        return user_name, "*" * len(pass1)  # Vraciame meno + hviezdičkovú dĺžku hesla
    else:
        print("Nie ste úspešne zaregistrovaný")
        return None, None  # Neúspešná registrácia


# Zoznam úspešne registrovaných
registrovani_pouzivatelia = []

# Spustenie registrácie
meno, heslo_maskovane = registracia()
if meno:
    registrovani_pouzivatelia.append(meno)  # Pridáme meno do zoznamu
    # Zapíšeme meno a dĺžku hesla (hviezdičky) do súboru
    with open("registrovani.txt", "a", encoding="utf-8") as file:
        file.write(f"{meno} - {heslo_maskovane}\n")
else:
    exit()  # Ukončíme program, ak registrácia nebola úspešná

# Výpis registrovaných
print("Registrovaní používatelia:", registrovani_pouzivatelia)

# Výpis obsahu súboru
print("Používatelia v súbore:")
with open("registrovani.txt", "r", encoding="utf-8") as file:
    print(file.read())



#písane mnou
c=random. randint(1,8)
print("Dobrý deň")
print("Dostal/a si číslo: " + str(c)) 
print("Napíš číslo ktoré si dostal/a a stlač enter")

if "a=0":
    while(True):
        a=int(input()) 
        if a!=c:
            continue
        vysledok=a**2
        print(f"skupinové číslo= {vysledok}")
        if vysledok>10:
            print ("Patríš do prvej skupiny")
            c=random. randint(50,99)
            print(f"Dostal si poradové číslo: {c}")
        else:
            print("Patríš do druhej skupiny")
            c=random. randint(1,49)
            print(f"Dostal si poradové číslo: {c}") 
        print("Prosím počkaj pokým zahlásia tvoje poradové číslo")
        print("Tvoj výdajný automat")
        
        break

else:
    print ("Nezadal si platný znak!")
    

        

