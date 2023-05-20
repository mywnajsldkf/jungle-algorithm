import sys
from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

# 상 - 우 - 하 - 좌
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def turn(order):
    if order == "L":  # 왼쪽
        if direction == 0:  # 위쪽을 보고 있었다면
            return 3
        elif direction == 1:  # 오른쪽을 보고 있었다면
            return 0
        elif direction == 2:  # 아래쪽을 보고 있었다면
            return 1
        elif direction == 3:  # 왼쪽을 보고 있었다면
            return 2
    elif order == "D":  # 오른쪽
        if direction == 0:
            return 1
        elif direction == 1:
            return 2
        elif direction == 2:
            return 3
        elif direction == 3:
            return 0

def start():
    direction = 1   # 초기 방향
    time = 1
    y, x = 0, 0     # 초기 뱀 위치
    # 뱀 움직임 저장
    snake = deque()
    snake.append((y, x))    # 움직임을 시작하는 뱀의 최초 위치를 저장한다.
    board[0][0] = 2  # 뱀이 차지함

    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
            if not board[y][x] == 2:    # 사과가 없는 경우
                temp_y, temp_x = snake.popleft()    # 꼬리 제거
            board[y][x] = 1
            snake.append()




if __name__ == "__main__":
    N = int(s.readline())  # 보드의 크기
    K = int(s.readline())  # 사과의 위치

    # 1. 그래프를 모두 0으로 채워준다.
    board = [[0 for _ in range(N)] for _ in range(N)]

    # 2. 그래프에 사과 위치를 2로 채워준다.
    for i in range(K):
        col, row = map(int, s.readline().split())
        board[col - 1][row - 1] = 2

    # 이동을 저장한다.
    L = int(s.readline())
    move = dict()
    for j in range(L):
        x, c = s.readline().split()
        move[int(x)] = c

    print(start())