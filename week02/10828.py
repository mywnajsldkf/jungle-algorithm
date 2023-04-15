from sys import stdin as s

s = open("input.txt", "rt")
N = int(s.readline())

stack = []

for i in range(N):
    line = list(s.readline().split())

    if line[0] == "push":
        stack.append(int(line[1]))
    elif line[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif line[0] == "size":
        print(len(stack))
    elif line[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())