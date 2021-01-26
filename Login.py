
print("Hallo! Wilkommen beim Login! Bitte die nun folgenden Fragen wahrheitsgemäß beantworten: ")

user = ["username", "password", 1990, 3, 18, "lfarbe", "notes"]
def correctinfo():

    correcting = True
    while correcting:

        corr = input("Was möchten Sie korrigieren? (Name, Geburtstag, Lieblingsfarbe, Notizen )")

        if corr == "Name":
            user[0] = input("Bitte Name eingeben: ")
            correcting = False

        elif corr == "Geburtstag":
            user[2] = int(input("Bitte Geburtsjahr eingeben: "))
            user[3] = int(input("Bitte Geburtsmonat eingeben: "))
            user[4] = int(input("Bitte Geburtstag eingeben: "))
            correcting = False

        elif corr == "Lieblingsfarbe":
            user[5] = input("Bitte Lieblingsfarbe eingeben: ")
            correcting = False

        elif corr == "Notizen":
            user[6] = input("Bitte Notizen eingeben: ")
            correcting = False

        else:
            print("Unbekannt")


def askcorr():

    print("Bitte überprüfe nun die Korrektheit deiner Angaben: ")
    print("Username: ", user[0])
    print("Geburtsdatum: ", user[2], user[3], user[4])
    print("Lieblingsfarbe: ", user[5])
    print("Notizen: ", user[6])
    correct2 = input("Sind deine Daten jetzt korrekt? (y/n)")

    if correct2 == "y":
        print("Sehr gut!")

    elif correct2 == "n":
        correctinfo()

    else:
        askcorr()


def register():

    user[0] = input("Bitte Benutzername eingeben: ")
    user[1] = (input("Bitte Passwort eingeben: "))
    user[2] = int(input("Bitte Geburtsjahr angeben: "))
    if user[2] < 1920:
        print("Das glaube ich dir nicht!")
        user[2] = int(input("Bitte Geburtsjahr angeben: "))

    user[3] = int(input("Bitte Geburtsmonat angeben: "))
    if user[3] > 12:
        print("Das ist unmöglich!")
        user[3] = int(input("Bitte Geburtsmonat angeben: "))

    user[4] = int(input("Bitte Geburtstag angeben: "))
    if user[4] > 31:
        print("Das ist unmöglich!")
        user[4] = int(input("Bitte Geburtstag angeben: "))

    user[5] = input("Bitte Lieblingsfarbe angeben: ")
    user[6] = input("Wenn du möchtest, kannst du nun noch Notizen zu dir hinzufügen. Sonst schreibe '-'")


while True:

    regorlog = input("Möchten Sie sich registrieren (r) oder einloggen (l): ")

    if regorlog == "r":

        register()

        print("Bitte überprüfe nun die Korrektheit deiner Angaben: ")
        print("Username: ", user[0])
        print("Geburtsdatum: ", user[2], user[3], user[4])
        print("Lieblingsfarbe: ", user[5])
        print("Notizen: ", user[6])

        correct = input("Sind deine Angaben korrekt?: (y/n) ")
        if correct == "y":
            print("Perfekt!")

        if correct == "n":
            neworcorr = input("Möchten Sie von vorne beginnen, oder etwas ausbessern? (new/corr)")

            if neworcorr == "new":
                register()
                askcorr()

            elif neworcorr == "corr":

                correctinfo()
                askcorr()

    elif regorlog == "l":

        x = 0
        y = 0
        tlogname = input("Bitte Benutzername eingeben: ")
        tpassword = input("Bitte Passwort eingeben: ")

        if tlogname == user[0]:
            x = x + 1

        elif tlogname == "Testperson":
            y = y + 1

        else:
            print("Flasche Angaben")

        if tpassword == user[1]:
            x = x + 1

        elif tpassword == "test":
            y = y + 1

        else:
            print("Falsche Angaben")

        if x == 2:
            print("Wilkommen zurück,", user[0])

        elif y == 2:
            print("Hallo :D")

        else:
            print("Fehler!")
    else:
        quit()
