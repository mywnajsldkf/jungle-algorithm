from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())

stack = []

count = 1
for i in range(N-1):
    stack.append(int(s.readline()))

base = int(s.readline())

while(len(stack) != 0):
    temp = stack.pop()

    if base < temp:
        count += 1
        base = temp

print(count)