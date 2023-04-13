import sys
from sys import stdin as s

N = int(s.readline())

l = [list(map(int, s.readline().split())) for _ in range(N)]

visit = [False]*N
m = sys.maxsize

def dfs(depth, start, cost):
    global m
    # 만약 시작지점을 0이 아닌 곳에서 시작했다면
    '''
    if depth == N-1 and l[start][1] != 0:
        m = min(m, cost+l[start][1])
        return
    '''

    if depth == N-1 and l[start][0] != 0:   # depth를 모두 확인했고, 되돌아갈 수 있다면
        m = min(m, cost+l[start][0])
        return
    for i in range(N):
        if not visit[i] and l[start][i] != 0:
            visit[i] = True
            dfs(depth+1, i, cost+l[start][i])
            visit[i] = False

# 만약 시작지점을 0이 아닌 곳에서 시작했다면
'''
visit[1] = True
dfs(0,1,0)
'''

visit[0] = True
dfs(0,0,0)
print(m)
