import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = a * b * c
numbers = [0,0,0,0,0,0,0,0,0,0]

for i in list(str(result)):
    numbers[int(i)] += 1

for i in numbers:
    print(i)