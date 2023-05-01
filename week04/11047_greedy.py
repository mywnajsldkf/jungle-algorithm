from sys import stdin as s
import sys

s = open("input.txt", "rt")

n, k = map(int, s.readline().split())
coin = []

for i in range(n):
    coin.append(int(s.readline()))

ans = 0
count = 0
a = len(coin) - 1
while k != 0:
    for i in range(a, -1, -1):
        if k - coin[i] >= 0:
            count += k // coin[i]
            k = int(k % coin[i])

print(count)