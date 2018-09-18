# skref 1: segja notenda frá hreyfingarmöguleikum.
# skref 2: taka inn "n" "s" "e" eða "e" og færa "leikmann"
# skref 3: ef einhvað annað kemur inn þá skal prenta viðeigana setningu.
# skref 4: ef leikmaður sló inn vitlausan staf þá fær hann að gera aftur, 
# eftir að setning í skrefi 3 hefur verið prentuð
# skref 5: gera while lykkju sem fer í gegnum if setningar þar sem while greinir hvaða reit leikmaður er á.
# skref 6: þegar leikmaður hefur komist á endareit, 3.1 þá prentum við út sigursetningu og lokuð prógramminu. 

position = 1

while True:
    print("You can travel: " , end="")
    if position == 4:
        print("(N)orth or (E)ast or (S)outh.")
        new_position = input("Direction: ")
        if new_position.upper() == "N":

            position = 7
        elif new_position.upper() == "S":

            position = 1
        elif new_position.upper() == "E":

            position = 5
        else:
            print("Not a valid direction!")

    if position == 1:
        print("(N)orth. ")
        new_position = input("Direction: ")
        if new_position.upper() == "N":
            print(" your position is 1,2")
            position = 4
        else:
            print("Not a valid direction!")

    if position == 5:
        print("(S)outh or (W)est. ")
        new_position = input("Direction: ")
        if new_position.upper() == "S":

            position = 2
        elif new_position.upper() == "W":

            position = 4
        else:
            print("Not a valid direction!")

    if position == 2:
        print("(N)orth. ")
        new_position = input("Direction: ")
        if new_position.upper() == "N":
            print(" your position is 2,2")
            position = 5
        else:
            print("Not a valid direction!")

    if position == 7:
        print("(S)outh or (E)ast.")
        new_position = input("Direction")
        if new_position.upper() == "S":
            print(" your position is 1,2")
            position = 4
        elif new_position.upper() == "E":
            print(" your position is 2,3")
            position = 8
        else:
            print("Not a valid direction!")

    if position == 8:
        new_position = input("You can travel: (E)ast or (W)est. ")
        if new_position.upper() == "E":
            print(" your position is 3,3")
            position = 9
        elif new_position.upper() == "W":
            print(" your position is 1,3")
            position = 7
        else:
            print("Not a valid direction!")

    if position == 9:
        new_position = input("You can travel: (S)outh or (W)est. ")
        if new_position.upper() == "S":
            print(" your position is 3,2")
            position = 6
        elif new_position.upper() == "W":
            print(" your position is 2,3")
            position = 8
        else:
            print("Not a valid direction!")

    if position == 6:
        new_position = input("You can travel: (N)orth or (S)outh. ")
        if new_position.upper() == "N":
            print(" your position is 3,3")
            position = 9
        elif new_position.upper() == "S":
            print(" your position is 3,1")
            position = 3
        else:
            print("Not a valid direction!")

    if position == 3:
        print("Victory!")
        break