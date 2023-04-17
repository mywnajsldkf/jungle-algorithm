from sys import stdin as s

s = open("../input.txt", "rt")

K, N = map(int, s.readline().split())

lanterns = []

for i in range(K):
    lanterns.append(int(s.readline()))

left = 1
right = max(lanterns)

while left <= right:
    mid = (left + right) // 2

    total = 0
    for lantern in lanterns:
        total += lantern // mid

    if total < N:   # 적어도 N개를 만드는 것이므로 total < N이면 false이다. -> 더 길이를 줄여야 한다.
        right = mid - 1
    elif total >= N:   # 적어도 N개를 만들면 true이다.
        left = mid + 1

print(right)