from sys import stdin as s

T = int(s.readline())

numbers = list(False for i in range(0,10001))    # 소수 O -> False / 소수 X -> True

for i in range(2, 10001):
    if(numbers[i] == False):
        for j in range(2*i, 10001, i):
            numbers[j] = True

for i in range(T):

    n = int(s.readline())

    first = 0
    second = 0
    min = 10000

    for j in range(2, n//2 + 1):
        if(numbers[j] == False and numbers[n-j] == False):
            cha = n-j-j
            if(min > cha):
                min = cha
                first = j
                second = n-j
    print(first, second)