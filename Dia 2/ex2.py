

"""
checks if the input strings differ by only 1 char
if so returns the index
"""


def checkFor1DiffChar(str1, str2):
    diffList = [idx for idx, val in enumerate(str1) if (idx, val) not in enumerate(str2)]
    if len(diffList) == 1:
        return diffList[0]
    else:
        return -1


def removeCharFromString(idx, strg):
    return strg[:idx] + strg[idx+1:]


result = False
myfile = open('C:\\Users\\Bruno Reis\\Desktop\\AdventOfCode\\Dia 2\\input.txt', 'r')
contents = myfile.read().strip().splitlines()
myfile.close()
for line1 in contents:
    for line2 in contents:
        idx = checkFor1DiffChar(line1, line2)
        if idx != -1:
            res = removeCharFromString(idx, line1)
            result = True
            break
    if(result):
        break

print(res)
