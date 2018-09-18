# skref 1: segja notenda frá hreyfingarmöguleikum.
# skref 2: taka inn "n" "s" "e" eða "e" og færa "leikmann"
# skref 3: ef einhvað annað kemur inn þá skal prenta viðeigana setningu.
# skref 4: ef leikmaður sló inn vitlausan staf þá fær hann að gera aftur, 
# eftir að setning í skrefi 3 hefur verið prentuð
# skref 5: gera while lykkju sem fer í gegnum if setningar þar sem while greinir hvaða reit leikmaður er á.
# skref 6: þegar leikmaður hefur komist á endareit, 3.1 þá prentum við út sigursetningu og lokuð prógramminu.. 

#Finna stöðu á leikmanni
#setja inni while lykkju og taka inn hreyfingu
#reikna nýja stöðu
#kominn á enda reyt skrifa Victory!

position = 1

while position != 3:
    print("You can travel: " , end="")
    if position == 4:
        print("(N)orth or (E)ast or (S)outh.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 7
                break
            elif new_position.upper() == "S":
                position = 1
                break
            elif new_position.upper() == "E":
                position = 5
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")
    elif position == 1:
        print("(N)orth.")
        new_position = input("Direction: ")
        while True:

            if new_position.upper() == "N":
                position = 4
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")
    elif position == 5:
        print("(S)outh or (W)est. ")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "S":
                position = 2
                break
            elif new_position.upper() == "W":
                position = 4
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 2:
        print("(N)orth. ")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 5
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 7:
        print("(E)ast or (S)outh.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "S":
                position = 4
                break
            elif new_position.upper() == "E":
                position = 8
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 8:
        print("(E)ast or (W)est.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "E":
                position = 9
                break
            elif new_position.upper() == "W":
                position = 7
                break
            else:
                print("Not a valid direction!")
                ew_position = input("Direction: ")

    elif position == 9:
        print("(S)outh or (W)est.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "S":
                position = 6
                break
            elif new_position.upper() == "W":
                position = 8
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 6:
        print("(N)orth or (S)outh.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 9
                break
            elif new_position.upper() == "S":
                position = 3
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

print("Victory!")