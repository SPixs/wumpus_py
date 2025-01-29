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
L1 = None
O = None

# PRINT LOCATION & HAZARD WARNINGS
def print_location():
    for J in range(1, 6):
        for K in range(0, 3):
            if S[L[1]][K] != L[J]:
                continue
            if  J == 2:
                print("I SMELL A WUMPUS!")
            elif J == 3:
                print("I FEEL A DRAFT")
            elif J == 4:
                print("BATS NEARBY!")
    print(f"YOU ARE IN ROOM {L[1]}")
    print(f"TUNNELS LEAD TO {S[L1][0]} {S[L1][1]} {S[L1][2]}")
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

# LOCATE L ARRAY ITEMS
# 1-YOU,2-WUMPUS,3&4-PITS,5&6-BAT
# CHECK FOR CROSSOVERS (IE L(1)=L(2),ETC)
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
L1=L[1] # L contains the room number of player
print("HUNT THE WUMPUS")
# HAZARD WARNINGS & LOCATION
print_location()
# MOVE OR SHOOT
choose_option()
print(O)




