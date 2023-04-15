import sys
from sys import stdin as s

s = open("input.txt", "rt")

T = int(s.readline())

for j in range(T):
    data = s.readline().rstrip()
    stack = []
    result = "YES"
    for i in range(len(data)):
        if data[i] == "(":
            stack.append('0')
        elif data[i] == ")" and len(stack) > 0:
            stack.pop()
        elif data[i] == ")" and len(stack) == 0:
            result = "NO"

    if len(stack) != 0:
        result = "NO"
    print(result)