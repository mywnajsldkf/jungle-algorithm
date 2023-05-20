from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline().rstrip())
paper = []

for i in range(N):
    paper.append(list(map(int, s.readline().rstrip().split())))

white = 0  # 하얀색: 0
blue = 0  # 파란색: 1

def find_square(y, x, length):
    global white, blue

    basis = paper[y][x]

    for i in range(y, y + length):
        for j in range(x, x + length):
            # 다른 지점이 생기면 -> 4분할하여 탐색한다.
            if paper[i][j] != basis:
                find_square(y, x, length // 2)
                find_square(y, x + length // 2, length // 2)
                find_square(y + length // 2, x, length // 2)
                find_square(y + length // 2, x + length // 2, length // 2)
                return
    if basis == 1:
        blue += 1
    elif basis == 0:
        white += 1

find_square(0, 0, N)
print(white)
print(blue)