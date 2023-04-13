from sys import stdin as s

N = int(s.readline())

numbers = []
for i in range(N):
    numbers.append(int(s.readline()))

numbers.sort()

for i in numbers:
    print(i)