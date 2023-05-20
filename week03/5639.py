from sys import stdin as s
import sys
sys.setrecursionlimit(10**9)
s = open("input.txt", "rt")

num_list = []
while True:
    try:
        num = int(s.readline())
        num_list.append(num)
    except:
        break


def postorder(first, end):
    if first > end:
        return
    mid = end + 1   # 오른쪽 노드가 없을 경우
    for i in range(first + 1, end + 1):
        if num_list[first] < num_list[i]:
            mid = i
            break

    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(num_list[first])


postorder(0, len(num_list) - 1)