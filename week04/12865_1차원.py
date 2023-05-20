from sys import stdin as s
import sys

s = open("input.txt", "rt")

n, k = map(int, s.readline().split())   # 물품 수, 준서가 버틸 수 있는 무게

# backpack = [[0 for _ in range(k+1)] for _ in range(n+1)]
backpack = [0 for _ in range(k+1)]

stuff = [[0, 0]]
for i in range(n):
    stuff.append(list(map(int, s.readline().split())))

for i in range(1, n+1):
    for j in range()

    weight = stuff[i][0]  # 물건의 무게
    value = stuff[i][1]  # 물건의 가치

    for j in range(1, k+1):     # 가방의 무게
        if j >= stuff[i][0]:
            backpack[j] = max(backpack[j - weight] + value, backpack[j])
    print(backpack)

print(backpack[k])

'''
for i in range(1, n+1):         # -> 물건의 무게
    for j in range(1, k+1):     # -> 가방의 무게
        weight = stuff[i][0]    # 무게
        value = stuff[i][1]     # 가치

        if j < weight:
            backpack[i][j] = backpack[i-1][j]
        else:
            backpack[i][j] = max(value + backpack[i-1][j-weight], backpack[i-1][j])

print(backpack[n][k])
'''
