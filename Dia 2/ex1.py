

counter = [0, 0]


myfile = open('C:\\Users\\Bruno Reis\\Desktop\\AdventOfCode\\Dia 2\\input2.txt', 'r')

for line in myfile:
    flag2 = False
    flag3 = False
    for l in line.lstrip():
        numOcurrs = line.count(l)
        if numOcurrs == 2 and not flag2:
            counter[0] += 1
            flag2 = True
        elif numOcurrs == 3 and not flag3:
            counter[1] += 1
            flag3 = True
        if flag2 and flag3:
            break


checksum = counter[0]*counter[1]
print(counter[0])
print(counter[1])
print(checksum)
