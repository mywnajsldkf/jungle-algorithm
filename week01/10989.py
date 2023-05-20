from sys import stdin as s

N = int(s.readline())

numbers = [0 for i in range(10000+1)]

for i in range(N):
    numbers[int(s.readline())] += 1

for i in range(1, 10001):
    while(numbers[i] > 0):
        print(i)
        numbers[i] -= 1