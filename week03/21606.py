from sys import stdin as s
from sys import setrecursionlimit
setrecursionlimit(10**9)
# recursiontimelimit 사용 덕분에 시간 단축 가능

s = open("input.txt", "rt")

N = int(s.readline().rstrip())
location = [0] + list(map(int, s.readline().rstrip()))
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
answer = 0


# graph 배열을 만든다.
for i in range(N-1):
    a, b = map(int, s.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    # 둘다 실내인 경우
    if location[a] == 1 and location[b] == 1:
        answer += 2

# v: 정점 번호, count: 실외와 연결된 실내 노드 개수
def dfs(v, count):
    visited[v] = True

    for i in graph[v]:
        if location[i] == 1:
            count += 1
        # 방문안했고, 0이라면(실외) -> 탐색한다.
        elif not visited[i] and location[i] == 0:
            count = dfs(i, count)
    return count

sum = 0
for i in range(1, N+1):
    # 실외를 기준으로
    if not visited[i] and location[i] == 0:
        x = dfs(i, 0)   # 현재 cnt는 0
        sum += x * (x-1)

print(sum + answer)