from sys import stdin as s
from collections import deque
s = open("input.txt", "rt")

N = int(s.readline())

a = []
queue = deque(a)

for i in range(N):
    queue.append(i+1)

'''
while(len(queue) > 1):
    
'''
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())