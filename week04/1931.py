from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

meeting = []

for i in range(n):
    start, finish = map(int, s.readline().split())
    meeting.append([start, finish])

meeting.sort(key=lambda meeting: (meeting[1], meeting[0]))


def greedySchedule():
    count = 1
    last = meeting[0][1]

    for m in range(1, n):
        if meeting[m][0] >= last:
            count += 1
            last = meeting[m][1]
    return count


print(greedySchedule())