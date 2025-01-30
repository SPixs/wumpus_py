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

L = [] # ROOMS INDEX OF (player, wumpus, pit, pit, bats, bats)
O = None # ACTION (1=SHOOT, 2=MOVE)
F = 0 # GAME STATUS FLAG
A = None # ARROWS

# PRINT LOCATION & HAZARD WARNINGS
def print_location():
    print()
    for J in range(1, 6):
        for K in range(0, 3):
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
    while True:
        I = input("SHOOT OR MOVE (S-M) ")
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
            LOC = input("WHERE TO ")
            if (LOC.isdigit()):
                LOC = int(LOC)-1
                if (LOC >= 0 and LOC < 20):
                    break
        
        # CHECK IF LEGAL MOVE
        valid = LOC == L[0] or any(S[L[0]][K] == LOC + 1 for K in range(3))

        if not valid:
            print("NOT POSSIBLE - ", end='')
        else:
            L[0] = LOC 

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

# ARROW ROUTINE
def shoot():
    global F, A 
    F = 0
    # PATH OF ARROW
    while True:
        J = input("NO. OF ROOMS(1-5) ")
        if J.isdigit():
            J = int(J)
            if J>0 and J<6:
                break

    P = []
    for K in range(J):
        while True:
            PK = int(input("ROOM # "))-1
            if K >= 2:
                if (PK == P[K-2]):
                    print("ARROWS AREN'T THAT CROOKED - TRY ANOTHER ROOM")
                else:
                    P.append(PK)
                    break
            else: 
                P.append(PK)
                break
        
    # SHOOT ARROW
    ARROW_L = L[0]
    for K in range(J):
        path_found = False
        for K1 in range(3):
            path_found = path_found or S[ARROW_L][K1] == P[K]+1

        if path_found:
            ARROW_L = P[K]
        else:
            # NO TUNNEL FOR ARROW
            ARROW_L = S[ARROW_L][fnb()]
            
        # SEE IF ARROW IS AT L(0) (player) OR L(1) (wumpus)
        # WUMPUS HIT ?
        if P[K] == L[1]:
            print("AHA! YOU GOT THE WUMPUS!")
            F = 1
            return
        # PLAYER HIT ?
        if P[K] == L[0]:
            print("OUCH! ARROW GOT YOU!")
            F = -1
            return

    print("MISSED")
    move_wumpus()
    # AMMO CHECK
    A -= 1
    if A <= 0:
        F = -1

    return

# INSTRUCTIONS
def print_instructions():
    print("WELCOME TO 'HUNT THE WUMPUS'")
    print("  THE WUMPUS LIVES IN A CAVE OF 20 ROOMS. EACH ROOM")
    print("HAS 3 TUNNELS LEADING TO OTHER ROOMS. (LOOK AT A")
    print("DODECAHEDRON TO SEE HOW THIS WORKS-IF YOU DON'T KNOW")
    print("WHAT A DODECAHEDRON IS, ASK SOMEONE)")
    print()
    print("     HAZARDS:")
    print(" BOTTOMLESS PITS - TWO ROOMS HAVE BOTTOMLESS PITS IN THEM")
    print("     IF YOU GO THERE, YOU FALL INTO THE PIT (& LOSE!)")
    print(" SUPER BATS - TWO OTHER ROOMS HAVE SUPER BATS. IF YOU")
    print("     GO THERE, A BAT GRABS YOU AND TAKES YOU TO SOME OTHER")
    print("     ROOM AT RANDOM. (WHICH MIGHT BE TROUBLESOME)")
    print()
    print("     WUMPUS:")
    print(" THE WUMPUS IS NOT BOTHERED BY THE HAZARDS (HE HAS SUCKER")
    print(" FEET AND IS TOO BIG FOR A BAT TO LIFT).  USUALLY")
    print(" HE IS ASLEEP. TWO THINGS WAKE HIM UP: YOUR ENTERING")
    print(" HIS ROOM OR YOUR SHOOTING AN ARROW.")
    print("     IF THE WUMPUS WAKES, HE MOVES (P=.75) ONE ROOM")
    print(" OR STAYS STILL (P=.25). AFTER THAT, IF HE IS WHERE YOU")
    print(" ARE, HE EATS YOU UP (& YOU LOSE!)")
    print()
    print("     YOU:")
    print(" EACH TURN YOU MAY MOVE OR SHOOT A CROOKED ARROW")
    print("   MOVING: YOU CAN GO ONE ROOM (THRU ONE TUNNEL)")
    print("   ARROWS: YOU HAVE 5 ARROWS. YOU LOSE WHEN YOU RUN OUT.")
    print("   EACH ARROW CAN GO FROM 1 TO 5 ROOMS. YOU AIM BY TELLING")
    print("   THE COMPUTER THE ROOM#S YOU WANT THE ARROW TO GO TO.")
    print("   IF THE ARROW CAN'T GO THAT WAY (IE NO TUNNEL) IT MOVES")
    print("   AT RAMDOM TO THE NEXT ROOM.")
    print("     IF THE ARROW HITS THE WUMPUS, YOU WIN.")
    print("     IF THE ARROW HITS YOU, YOU LOSE.")
    print()
    print("    WARNINGS:")
    print("     WHEN YOU ARE ONE ROOM AWAY FROM WUMPUS OR HAZARD,")
    print("    THE COMPUTER SAYS:")
    print(" WUMPUS-  'I SMELL A WUMPUS'")
    print(" BAT   -  'BATS NEARBY'")
    print(" PIT   -  'I FEEL A DRAFT'")
    print()

    return

# HUNT THE WUMPUS
# ORIGINAL GAME BY GREGORY YOB (1973)
# 1:1 PYTHON PORT BY SEBASTIEN MAMETZ (2025)
if input("INSTRUCTIONS (Y-N)" ).upper() == "Y":
    print_instructions()

# ANNOUNCE WUMPUSII FOR ALL AFICIONADOS ... ADDED BY DAVE
print()
print("     ATTENTION ALL WUMPUS LOVERS!!!")
print("     THERE ARE NOW TWO ADDITIONS TO THE WUMPUS FAMILY OF PROGRAMS.")
print()
print("     WUMP2:  SOME DIFFERENT CAVE ARRANGEMENTS")
print("     WUMP3:  DIFFERENT HAZARDS")
print()

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
    I = input("SAME SET-UP (Y-N) ").upper()
    RESET_CAVE = I != "Y"
    