from random import randint

# Setup cave

S = [ [2,5,8],[1,3,10],[2,4,12],[3,5,14],[1,4,6],
      [5,7,15],[6,8,17],[1,7,9],[8,10,18],[2,9,11],
      [10,12,19],[3,11,13],[12,14,20],[4,13,15],[6,14,16],
      [15,17,20],[7,16,18],[9,17,19],[11,18,20],[13,16,19] ]

def fna():
    return int(randint(0,19))

def fnb():
    return int(randint(0,2))

def fnc():
    return int(randint(0,3))

L = []
O = None
F = 0

# PRINT LOCATION & HAZARD WARNINGS
def print_location():
    print()
    for J in range(1, 6):
        for K in range(0, 3):
#            print(S[L[0]][K], " ", L[J])
            if S[L[0]][K] != L[J]+1:
                continue
            if  J == 1:
                print("I SMELL A WUMPUS!")
            elif J == 2 or J == 3:
                print("I FEEL A DRAFT")
            elif J == 4 or J == 5:
                print("BATS NEARBY!")
    LOC = L[0]
    print(f"YOU ARE IN ROOM {L[0]+1}")
    print(f"TUNNELS LEAD TO {S[LOC][0]} {S[LOC][1]} {S[LOC][2]}")
    print()
    return

def choose_option():
    global O
    print("SHOOT OR MOVE (S-M)")
    while True:
        I = input()
        if I == "S" or I == "s":
            O = 1
            return
        elif I == "M" or I == "m":
            O = 2
            return

    return

def move_wumpus():
    global F
    K = fnc()
    if K < 3:
        L[1] = S[L[1]][K]-1
    if L[1] == L[0]:
        print("TSK TSK TSK- WUMPUS GOT YOU!")
        F = -1
    return

def move():
    global F
    F=0 
    valid = False
    while not valid:
        while True:
            print("WHERE TO")
            LOC = input()
            if (LOC.isdigit()):
                LOC = int(LOC)-1
                if (LOC >= 0 and LOC < 20):
                    break
        
        # CHECK IF LEGAL MOVE
        valid = LOC == L[0] or any(S[L[0]][K] == LOC + 1 for K in range(3))

        if not valid:
            print("NOT POSSIBLE -")
        else:
            L[0] = LOC 

#    print("L=",L)

    # CHECK FOR HAZARDS
    while True:
        # WUMPUS ?
        if (L[0] == L[1]):
            print("...OOPS! BUMPED A WUMPUS!")
            move_wumpus()
            if (F != 0):
                return
        
        # PIT ?
        elif (L[0] == L[2] or L[0] == L[3]):
            print("YYYIIIIEEEE . . . FELL IN PIT")
            F = -1
            return

        # BATS ?
        elif (L[0] == L[4] or L[0] == L[5]):
            print("ZAP--SUPER BAT SNATCH! ELSEWHEREVILLE FOR YOU!")
            L[0] = fna()
        else:
            return
    
    return

def shoot():
    return

RESET_CAVE = True
while True:

    if (RESET_CAVE):
        # LOCATE L ARRAY ITEMS
        # 1-YOU,2-WUMPUS,3&4-PITS,5&6-BAT
        # CHECK FOR CROSSOVERS (IE L[0]=L[1],ETC)
        while True:
            cross_over = False 
            L.clear()
            L.extend(fna() for _ in range(6))
            M = list(L)
            for j in range(6):
                for k in range(6):
                    if j==k:
                        continue
                    if L[j] == L[k]:
                        cross_over = True
                        break
            if not cross_over:
                break

    # ARROWS
    A=5
    L1=L[0] # L contains the room number of player
    print("HUNT THE WUMPUS")
    # HAZARD WARNINGS & LOCATION
    while True:
        print_location()
        # MOVE OR SHOOT
        choose_option()
        if O == 1:
            shoot()
        else:
            move()
        if F != 0:
            break

    # LOSE ?
    if F < 0:
        print("HA HA HA - YOU LOSE!")
    # WIN !    
    else:
        print("HEE HEE HEE - THE WUMPUS'LL GETCHA NEXT TIME!!")

    L = list(M)
    print("SAME SET-UP (Y-N)")
    I = input().upper()
    RESET_CAVE = I != "Y"
