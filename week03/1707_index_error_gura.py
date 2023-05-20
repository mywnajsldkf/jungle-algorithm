from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

K = int(s.readline())
now_color = 1  # 1: RED, 0: None, -1: FALSE
is_success = True
node = []


def color(_i):
    global now_color
    if node[_i] == 0:
        node[_i] = now_color
        now_color = -now_color
    elif node[_i] == now_color:
        now_color = -now_color
    elif node[_i] != now_color:
        return True


for t in range(K):
    V, E = map(int, s.readline().rstrip().split())
    node = [0] * (V + 1)

    for i in range(E):
        start, end = map(int, s.readline().rstrip().split())
        if color(start):
            is_success = False
            break
        if color(end):
            is_success = False
            break

    if is_success:
        print("YES")
    else:
        print("NO")

'''
이렇게 한다면, 첫번째 케이스에 다 받기도 전에 break를 만나 뒤에 있는 것이 막힐 수 있다.
'''