from sys import stdin as s
import sys

s = open("input.txt", "rt")

expression = s.readline().split('-')

for i in range(0, len(expression)):
    expression[i] = sum(list(map(int, expression[i].split('+'))))

result = expression[0]

for i in range(1, len(expression)):
    result -= expression[i]

print(result)