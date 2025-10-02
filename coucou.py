import re

TEST1 =\
"""3
2 2 3
"""

TEST2 =\
"""5
1 2 3 4 5
"""

TEST3 =\
"""7
4 4 4 4 7 7 7
"""

def recursive(dict, i):
    if i <= 1:
        return 1
    if i in dict:
        res = dict.get(i)
        if res != i:
            # print(res)
            return 1 + recursive(dict, res)
    else:
        return 1 + recursive(dict, i - 1)

def parsing(inputs):
    list_line = inputs.splitlines()
    nbr_of_intersection = list_line[0]
    shortcuts_string = list_line[1]
    # for nbr in shortcuts_string:
    list_of_shortcuts = re.findall(r'\d+', shortcuts_string)
    # print(list_of_shortcuts)
    dict = {}
    for j in range(len(list_of_shortcuts)):
        dict.update({j : int(list_of_shortcuts[j])})
    print("0 ", end="")
    result_list_inverse = []
    result = 1
    for j in range(int(nbr_of_intersection), 1, -1):
        # result_list_inverse.append(recursive(dict, j))
        result_list_inverse.append(j)
    result_list_inverse.append(0)
    for kndex in range(len(result_list_inverse) - 1, 0, -1):
        print(str(result_list_inverse[kndex]) + "", end="")

        # print(list_of_shortcuts[i - 1], " vs ", str(i))
        # if int(list_of_shortcuts[i - 1]) == i and i:
        #     # print("1 ", end="")
        #     print("1 ")
        #     short += 1
        # else:
        #     # print(str(i - 1) + " ", end="")
        #     print(str(i - 1) + " ")
    print("")

def tests():
    parsing(TEST1)
    parsing(TEST2)
    parsing(TEST3)

tests()