from sys import stdin as s

X = int(s.readline())

count = 0

if X >= 100:
    for i in range(100, X+1):
        number = list(str(i))
        result = []
        for j in number:
            result.append(int(j))

        cha = result[1] - result[0]
        isHansoo = False
        for j in range(2, 3):
            if(result[j]-result[j-1] == cha):
                isHansoo = True
            else:
                isHansoo = False

        if(isHansoo):
            count+=1

    print(99+count)


else:
    print(X)
