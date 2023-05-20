from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

# 0부터 9까지 숫자가 모두 등장하는 계단 수

if n < 10:
    print(0)
else:
