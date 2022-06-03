x = input("ISBN 1-9: ")
n1_9 = int(x[0])*10 + int(x[1])*9 + int(x[2])*8 + int(x[3])*7 + int(x[4])*6 + int(x[5])*5 + int(x[6])*4 + int(x[7])*3 + int(x[8])*2
n10 = 0
while True:
    n10+=1
    if (n1_9 + n10)%11 == 0 or n10 == 10 :
        break
x = x + str(n10)
print("ISBN 10: ",x)