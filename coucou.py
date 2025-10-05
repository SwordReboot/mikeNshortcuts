import re
import sys

input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return [char for char in s if char != " "]
def invr():
    return(map(int,input().split()))

# Challenge 1: find the biggest shortcut in the list - shouldn't need a recursive
# Challenge 2: continue the path until Mike's house in the inverse order without calling twice or more the list nor doing unecessarily stuff
# Challenge 3: the need of going croissant for the shortcut list and decroissant for the right shortest path
# arg house_end is the last intersection Mike would like to go and through recursivity, its path (intersection number) leading to it
def recu(list_of_shortcuts, house_end) -> int:
    # Mike starts at his house at intersection 1
    # Here at value 0 as it's used for list index so -1
    house_begin = 0
    # Read the shortcut list in the croissant ( < ) order to catch the biggest shortcut
    for j in range(house_begin, house_end):
        # Debug printing: if there wasn't any shortcut
        # print(str(i - house_begin) + " ", end="")
        # if 
        if int(list_of_shortcuts[j]) == house_end:
            # Avoiding listed "shortcuts" like a roundabout without exit (distance == 0) or shortcuts=2h42min and path=2h42min (distance == 1) :/
            if house_end - (j+1) >= 2:
                # Debug printing: finding shortcuts and keeping them
                # print("shortcut found: " + list_of_shortcuts[j] + " to " + str(j+1))
                # Shortcut to j+1 found, let's find again shortcuts from j+1 to ... ultimately first intersection - Mike's house
                # And add one - shortcut or path, still took some energy walking
                return 1 + recu(list_of_shortcuts, j+1)
    # Still not at Mike's house, let's continue finding it, and add 1 to result as walking is tiring, and -1 for being closer to Mike's house <3
    # 2 is the first intersection after Mike's intersection - n°1
    if house_end >= 2:
        return 1 + recu(list_of_shortcuts, house_end - 1)
    # Mike's house - or first intersection - found ! No need to add one
    return 0

def find_path(nbr_of_intersection: int, list_of_shortcuts: list[str]) -> None:
    # Output asks to check all intersections
    for i in range(nbr_of_intersection):
        # Debug printing: for creating algorithm, always check at which intersection the algo is
        # print("intersection n° " + str(i))
        # Calling recursive and printing its path result without changing line
        # i+1 because the for loop stops one early, as house intersection starts at 1 and not 0 - one day, you will be recognised as a number RIP -
        print(str(recu(list_of_shortcuts, i+1)) + " ", end="")
    # End of all intersections in Mike's house's city
    print("")

def main():
    # Input: Number of intersections - int
    first = inp()
    # Input: List of shortcuts - list[str]
    second_list = insr()
    # Calling computation of laziness
    find_path(first, second_list)
# main()

# visual checking
def tests():
    find_path(3, ["2", "2", "3"])
    print("0 1 2 <== does it look the same?")
    find_path(5, ["1", "2", "3", "4", "5"])
    print("0 1 2 3 4 <== does it look the same?")
    find_path(7, ["4", "4", "4", "4", "7", "7", "7"])
    print("0 1 2 1 2 3 3 <== does it look the same?")
    # WIP
    find_path(98, ["17", "17", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "57", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "87", "90", "90", "90", "90", "90", "90", "90", "90", "90", "90", "90", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "92", "95", "95", "95", "95", "95", "97", "98", "98"])
    print("0 1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 4 4 5 6 5 6 7 8 <== does it look the same?")

tests()
