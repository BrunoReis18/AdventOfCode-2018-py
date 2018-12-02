
sum = 0
S = set()
flag = True
while(flag):
    myfile = open('C:\\Users\\Bruno Reis\\Desktop\\AdventOfCode\\Dia 1\\input2.txt', 'r')
    for line in myfile:
        sum += int(line)
        print(sum)
        if(sum in S):
            flag = False
            print("Lesgo")
            break
        S.add(sum)
