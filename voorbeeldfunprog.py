from tabulate import tabulate
from colorama import *

personeel = {"p1":{"naam":"Michael Scott","geslacht":"m","startjaar":2000,"afdeling":"Management","loon":5000},
             "p2":{"naam":"Dwight Schrutte","geslacht":"m","startjaar":2004,"afdeling":"Sales","loon":2700},
             "p3":{"naam":"Jim Halpert","geslacht":"m","startjaar":2004,"afdeling":"Sales","loon":2700},
             "p4":{"naam":"Pam Beesly","geslacht":"v","startjaar":2006,"afdeling":"Reception","loon":1800},
             "p5":{"naam":"Kevin Malone","geslacht":"m","startjaar":2005,"afdeling":"Accounting","loon":2400},
             "p6":{"naam":"Angela Martin","geslacht":"v","startjaar":2004,"afdeling":"Accounting","loon":2500},
             "p7":{"naam":"Oscar Martines","geslacht":"m","startjaar":2007,"afdeling":"Accounting","loon":2250},
             "p8":{"naam":"Kelly Kapoor","geslacht":"v","startjaar":2008,"afdeling":"Customers Service","loon":1700},
             "p9":{"naam":"Ryan Howard","geslacht":"m","startjaar":2009,"afdeling":"Trainee","loon":0},
             "p10":{"naam":"Toby Flenderson","geslacht":"m","startjaar":2004,"afdeling":"HR","loon":2500},
             }
admin_ingelogd = "nee"
admins = {"id 0":{"username":"admin","password":"admin"}}
filter_dict = {}

####filters

def filter_startjaar():
    startjaar = int(input("vanaf welk startjaar filter je"))
    for id, employer in personeel.items():
        if startjaar > employer["startjaar"]:
            filter_dict.update(
                    {id: {"naam": employer["naam"], "geslacht": employer["geslacht"],
                            "afdeling": employer["afdeling"], "startjaar": employer["startjaar"],
                            "loon": employer["loon"]}})
    tabel = []
    tabel.append(["Personeelsnummer", "Naam", "Geslacht","Startjaar","afdeling","loon"])
    for wn, wn_data in filter_dict.items():
        tabel.append([wn, wn_data["naam"],wn_data["geslacht"],wn_data["startjaar"],
                      wn_data["afdeling"],wn_data["loon"]])
    print(tabulate(tabel, headers="firstrow", tablefmt="pretty"))
    print(len(filter_dict))

def filter_loon():
    loon = int(input("vanaf welk loon filter je"))
    for id, employer in personeel.items():
        if loon < employer["loon"]:
            filter_dict.update(
                    {id: {"naam": employer["naam"], "geslacht": employer["geslacht"],
                            "afdeling": employer["afdeling"], "startjaar": employer["startjaar"],
                            "loon": employer["loon"]}})
    tabel = []
    tabel.append(["Personeelsnummer", "Naam", "Geslacht","Startjaar","afdeling","loon"])
    for wn, wn_data in filter_dict.items():
        tabel.append([wn, wn_data["naam"],wn_data["geslacht"],wn_data["startjaar"],
                      wn_data["afdeling"],wn_data["loon"]])
    print(tabulate(tabel, headers="firstrow", tablefmt="pretty"))
    print(len(filter_dict))



def filter_mv():
    gender = input("Do you want to see all men or women? (man / woman)")
    print(Fore.RESET)
    if gender.lower() == "m" or gender.lower() == "v":
        for id, employer in personeel.items():
            if employer["geslacht"] == gender:
                filter_dict.update(
                    {id: {"naam": employer["naam"], "geslacht": employer["geslacht"],
                            "afdeling": employer["afdeling"], "startjaar": employer["startjaar"],
                            "loon": employer["loon"]}})
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET)

    tabel = []
    tabel.append(["Personeelsnummer", "Naam", "Geslacht","Startjaar","afdeling","loon"])
    for wn, wn_data in filter_dict.items():
        tabel.append([wn, wn_data["naam"],wn_data["geslacht"],wn_data["startjaar"],
                      wn_data["afdeling"],wn_data["loon"]])
    print(tabulate(tabel, headers="firstrow", tablefmt="pretty"))

def filter_afdeling():
    keuze = input("geef aan wie in welke afdeling werkt")
    for id,employer in personeel.items():
        if employer["afdeling"] == keuze:
            filter_dict.update(
                    {id: {"naam": employer["naam"], "geslacht": employer["geslacht"],
                            "afdeling": employer["afdeling"], "startjaar": employer["startjaar"],
                            "loon": employer["loon"]}})
    tabel = []
    tabel.append(["Personeelsnummer", "Naam", "Geslacht","Startjaar","afdeling","loon"])
    for wn, wn_data in filter_dict.items():
        tabel.append([wn, wn_data["naam"],wn_data["geslacht"],wn_data["startjaar"],
                      wn_data["afdeling"],wn_data["loon"]])
    print(tabulate(tabel, headers="firstrow", tablefmt="pretty"))



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
    keuze_f = input("geef keuze")
    while not keuze_f == "exit":

        if keuze_f == "1":
            filter_mv()
        elif keuze_f == "2":
            filter_afdeling()
        elif keuze_f == "3":
            filter_loon()
        elif keuze_f == "4":
            filter_startjaar()
        else:
            print("foutieve invoer")
            toon_filter_menu()

def toon_personeel():
    tabel = []
    tabel.append(["Personeelsnummer", "Naam", "Geslacht","Startjaar","Afdeling","Jaarloon"])
    for wn, wn_data in personeel.items():
        tabel.append([wn, wn_data["naam"],wn_data["geslacht"],wn_data["startjaar"],
                      wn_data["afdeling"],wn_data["loon"]*12])
    print(tabulate(tabel, headers="firstrow", tablefmt="pretty"))

def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def admin_login():
    username = input("Enter your username as admin:")
    password = input("Enter your password:")
    for id, employer in admins.items():
        while not password == employer["password"] or not username == employer['username']:
            print(Fore.RED, "\nIncorrect login credentials!", Fore.RESET)
            username = input("\n\nEnter your username again as admin:")
            password = input("Enter your password:")
    print(Fore.BLACK)
    print("-----------------------------------------------------------------------------------------------------------"
          "-")
    print(Fore.LIGHTGREEN_EX)
    print("\t\t\t\t\t\t\t\t\t\t\t\tADMIN LOGIN SUCCESSFUL\n")
    for id, employer in admins.items():
        username = employer['username']
        text = employer['password']
        s = 4
    print(Fore.LIGHTGREEN_EX, "\n\t\t\t\t\t\t\t\t\t\t\t\tUsername: " + username)
    print("\t\t\t\t\t\t\t\t\t\t\t\tPassword (encrypted): " + encrypt(text, s))
    encrypt("admin", 4)
    print(Fore.BLACK, "------------------------------------------------------------------------------------------------"
                      "-----------", Fore.LIGHTGREEN_EX)
    print(Fore.RESET)


def voeg_een_persoon_toe(personeel):
    naam = input("Geef de naam van de medewerker: ")
    geslacht = input("Geef het geslacht van de medewerker: ")
    afdeling = input("Geef de afdeling van de medewerker: ")
    jaar_indiensttreding = int(input("Geef het jaar van indiensttreding van de medewerker: "))
    maandloon = int(input("Geef het maandloon van de medewerker: "))
    nieuw_id = "p" + str(len(personeel) + 1)
    personeel[nieuw_id] = {"naam": naam, "geslacht": geslacht, "afdeling": afdeling, "startjaar": jaar_indiensttreding, "loon": maandloon}

def voeg_aantal_personen_toe():
    aantal_personen = int(input("geef het aantal in"))
    for persoon in range(aantal_personen):
        voeg_een_persoon_toe(personeel)

def verwijder_personeelslid():
    toon_personeel()
    pers_id = input("geef het id")
    if pers_id in personeel:
        personeel.pop(pers_id)
    else:
        print("id niet gevonden")

def verhoog_loon():
    toon_personeel()
    id = input("geef het id in waarvan het loon wilt verhogen")
    if id in personeel:
        nieuwe_loon = int(input("geef het loon in"))
        personeel[id]["loon"] = nieuwe_loon
    else:
        print("id niet gevonden")
        verhoog_loon()

def verhoog_alle_loon():
    extra_loon = int(input("geef aan hoeveel u extra wilt geven per maand"))
    for id,persoon in personeel.items():
         persoon["loon"] += extra_loon


####################################
#Hoofdprogramma
####################################
def hoofdprogramma():
    toon_menu()
    keuze = input("geef je keuze in")
    while not keuze == "stop":
        if keuze == "1":
            toon_personeel()
        elif keuze == "2":
            admin_login()
            toon_menu_admin()

        elif keuze == "3":
            toon_filter_menu()
        elif keuze == "a1":
            voeg_een_persoon_toe(personeel)
        elif keuze == "a2":
            voeg_aantal_personen_toe()
        elif keuze == "a3":
            verwijder_personeelslid()
        elif keuze =="a4":
            verhoog_loon()
        elif keuze == "a5":
            verhoog_alle_loon()
        else:
            print("foute invoer")
        toon_menu()
        keuze = input()

hoofdprogramma()
