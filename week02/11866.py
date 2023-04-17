from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

n, k = map(int, s.readline().split())

result = deque([_+1 for _ in range(n)])

print('<', end='')

while result:
    for i in range(k-1):
        result.append(result[0])
        result.popleft()
    print(result.popleft(), end='')
    if result:
        print(', ', end='')
print('>')