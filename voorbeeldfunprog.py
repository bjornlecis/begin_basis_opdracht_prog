from tabulate import tabulate
personeel = {"p1":{"naam":"Michael Scott","geslacht":"m","startjaar":2000,"afdeling":"Management","loon":5000},
             "p2":{"naam":"Dwight Schrutte","geslacht":"m","startjaar":2004,"afdeling":"Sales","loon":2700},
             "p3":{"naam":"Jim Halpert","geslacht":"M","startjaar":2004,"afdeling":"Sales","loon":2700},
             "p4":{"naam":"Pam Beesly","geslacht":"V","startjaar":2006,"afdeling":"Reception","loon":1800},
             "p5":{"naam":"Kevin Malone","geslacht":"M","startjaar":2005,"afdeling":"Accounting","loon":2400},
             "p6":{"naam":"Angela Martin","geslacht":"V","startjaar":2004,"afdeling":"Accounting","loon":2500},
             "p7":{"naam":"Oscar Martines","geslacht":"M","startjaar":2007,"afdeling":"Accounting","loon":2250},
             "p8":{"naam":"Kelly Kapoor","geslacht":"V","startjaar":2008,"afdeling":"Customers Service","loon":1700},
             "p9":{"naam":"Ryan Howard","geslacht":"M","startjaar":2009,"afdeling":"Trainee","loon":0},
             "p10":{"naam":"Toby Flenderson","geslacht":"M","startjaar":2004,"afdeling":"HR","loon":2500},
             }

admins = {"admin":"the office"}

def toon_menu():
    print("1 toon alle info")
    print("2 login als admin")
    print("3 gebruik een filter")

def toon_menu_admin():
    print("a1 voeg personeelslid toe")
    print("a2 voeg personeelsleden toe")
    print("a3 verwijder een personeelslids")
    print("a4 verhoog loon personeelslid")
    print("a5 verhoog alle lonen met")
    print("a6 toon admins")

def toon_filter_menu():
    print("1 toon m/v")
    print("2 toon afdeling")
    print("3 toon meer dan x per maand")
    print("4 in dienst voor ")

def toon_personeel():
    tabel = []
    tabel.append(["Personeelsnummer", "Naam", "Geslacht","Startjaar","Afdeling","Loon"])

    for wn, wn_data in personeel.items():
        tabel.append([wn, wn_data["naam"],wn_data["geslacht"],wn_data["startjaar"],
                      wn_data["afdeling"],wn_data["loon"]])
    print(tabulate(tabel, headers="firstrow", tablefmt="pretty"))

####################################
#Hoofdprogramma
####################################

toon_menu()
keuze = input("geef je keuze in")
while not keuze == "stop":
    if keuze == "1":
        break
    elif keuze == "2":
        break
    elif keuze == "3":
        break
    else:
        print("foute invoer")
    toon_menu()
    keuze = input()
