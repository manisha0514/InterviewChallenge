n = 100
for i in range(1,n):
    if (i % 3 ==0) and (i % 5 == 0):
        print('ThreeFive')
    elif i % 3 == 0:
        print("Three")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)