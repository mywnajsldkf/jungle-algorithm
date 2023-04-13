from sys import stdin as s

dy = [0,1,0,-1]
dx = [1,0,-1,0]

N = int(s.readline())

map = [[0]*N for i in range(N)]

max_count = 1

queue = []

# 영역 찾기
def bfs():
    # 동서남북 탐색 시작

    while(len(queue) != 0):
        point = queue.pop()
        now_y = point[0]
        now_x = point[1]
        for direction in range(4):
            next_y = now_y + dy[direction]
            next_x = now_x + dx[direction]

            # 범위 밖이라면 -> continue
            if(next_y < 0 or next_x < 0 or next_y >= N or next_x >= N):
                continue

            # 이미 잠겼다면
            if(sinked[next_y][next_x]):
                continue

            queue.append([next_y, next_x])
            sinked[next_y][next_x] = True

for i in range(N):
    temp = s.readline().split()
    for j in range(N):
        map[i][j] = int(temp[j])

for h in range(1, 100):
    count = 0
    # 초기화
    global sinked
    sinked = [[False]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if(map[i][j] <= h):
                sinked[i][j] = True
    for i in range(N):
        for j in range(N):
            if (sinked[i][j] == False):
                count += 1
                queue.append([i,j])
                bfs()

    if(max_count < count):
        max_count = count

print(max_count)