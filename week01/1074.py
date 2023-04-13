import math
from sys import stdin as s

global r
global c
N, r, c = map(int, s.readline().split())

global count
count = 0

# x, y는 시작 위치
def square(n, y, x):

    global count
    # x는 2보다 크면, 다시 돌아본다.
    if(n > 1):
        if(0 <= y and y < math.pow(2, n-1) and 0 <= x and x < math.pow(2, n-1)):
            # print("영역1")
            # print("x: ", x, "y: ", y)
            square(n-1, y, x)
        elif(0 <= y and y < math.pow(2, n-1) and math.pow(2,n-1) <= x and x < math.pow(2,n)):
            # print("영역2")
            # print("x: ", x, "y: ", y)
            count += math.pow(2, n-1) * math.pow(2, n-1)
            square(n-1, y, x - math.pow(2, n-1))
        elif(math.pow(2,n-1) <= y and y < math.pow(2, n) and 0 <= x and x < math.pow(2,n-1)):
            # print("영역3")
            # print("x: ", x, "y: ", y)
            count += 2 * math.pow(2, n-1) * math.pow(2, n-1)
            # print("count: ", count)
            square(n-1, y - math.pow(2, n-1), x)
        elif(math.pow(2, n-1) <= y and y < math.pow(2,n) and math.pow(2,n-1) <= x and x < math.pow(2,n)):
            # print("영역4")
            # print("x: ", x, "y: ", y)
            count += 3 * math.pow(2, n-1) * math.pow(2, n-1)
            # print("count: ", count)
            #
            # print(n//2, y-math.pow(2, n-1), x - math.pow(2,n-1))
            square(n-1, y-math.pow(2, n-1), x - math.pow(2, n-1))
    else:
        x = int(x)
        y = int(y)
        # print("x: ", x, "y: ", y)
        if(y == 0 and x == 0):
            count += 0
        elif(y == 0 and x == 1):
            count += 1
        elif(y == 1 and x == 0):
            count += 2
        elif(y == 1 and x == 1):
            count += 3

square(N, r, c)
print(int(count))