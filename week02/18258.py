from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

N = int(s.readline())

a = []
queue = deque(a)
for i in range(N):
    line = list(s.readline().split())
    if line[0] == "push":
        queue.append(int(line[1]))
    elif line[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif line[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif line[0] == "size":
        print(len(queue))
    elif line[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif line[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())