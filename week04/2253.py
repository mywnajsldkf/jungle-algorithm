from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n, m = map(int, s.readline().split())  # 돌의 개수 / 도달할 수 없는 작은 돌 개수
check = [[] for _ in range(n+1)]
small_rock = set()

for i in range(m):
    small_rock.add(int(s.readline()))

print(small_rock)

'''
def isPossible(x):
    # 범위 확인
    if x >= n:
        return False

    # 방문 가능한가
    if visited[x] is None:
        return False

    # 방문 여부 확인
    if visited[x] == -1:
        return True
'''



def bfs(start, end):
    queue = deque()
    queue.append((1, start))  # 위치, 얼마나 이동했는지
    # visited[start] = 2  # count 올린다.

    while queue:
        # print(queue.popleft())
        distance, now_x = queue.popleft()
        # print(distance, now_x)
        # print(now)
        # now_x = now[0]
        # distance = now[1]

        # print(distance - 1, distance, distance + 1)
        if now_x == end:
            return

        '''
        for move in [distance - 1, distance, distance]:
            next_x = now_x + move
            if next_x <= now_x:
                continue

            if isPossible(next_x):
                queue.append(next_x)
                visited[next_x] = visited[now_x] + 1
        '''

        '''
        for move in [dis - 1, dis, dis + 1]:
            next_x = now_x + move
            if next_x <= 0:
                continue

            # 도착지점이라면
            if next_x == end:
                return
            if isPossible(next_x):
                queue.append(next_x)
                visited[next_x] = visited[now_x] + 1

        '''
# bfs(2, n)