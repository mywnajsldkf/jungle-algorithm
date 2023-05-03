from sys import stdin as s
import sys

s = open("input.txt", "rt")

t = int(s.readline())

for i in range(t):
    n = int(s.readline())
    rank = []
    for j in range(n):
        rank.append(list(map(int, s.readline().split())))

    rank.sort(key=lambda x : x[0])

    top = 0
    result = 1

    for i in range(1, n):
        # i번째 사람에 대해서 0~i-1 번째 사람들과 면접 심사 결과를 비교했을 때, 더 높다면 채용이 된다.
        if rank[i][1] < rank[top][1]:
            # 모든 사람과 비교하는 것은 시간이 많이 들기 대문에
            # 가장 높은 사람의 순위랑 비교한다.
            top = i
            result += 1

    print(result)