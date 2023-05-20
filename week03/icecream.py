s = open("input.txt", "rt")

n, m = map(int, s.readline().split())

ice = []  # ice 배열 생성
visited = [[False for i in range(m)] for j in range(n)]  # 방문 배열 -> 방문한 점은 표시하기
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    line = s.readline().rstrip()
    ice.append(list(map(int, line)))
count = 0


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        # 범위 안에 포함되어 있는지 확인
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue
        # 이미 방문했는지 확인
        if visited[new_x][new_y]:
            continue
        # 범위 안에 포함되어 있고, 방문한 시점부터 탐색 시작!
        if ice[new_x][new_y] == 0:
            dfs(new_x, new_y)

for i in range(n):
    for j in range(m):
        if ice[i][j] == 0 and not visited[i][j]:
            count += 1
            dfs(i, j)


print(count)