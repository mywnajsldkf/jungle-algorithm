from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
A = list(map(int, s.readline().split()))

dp = [0]

def findNearest(key):
    left = 1
    right = len(dp)-1

    while left <= right:
        middle = (left + right) // 2
        if key == dp[middle]:
            return middle
        elif key < dp[middle]:
            right = middle - 1
        elif key > dp[middle]:
            left = middle + 1

    print("left:", left, "right:", right)
    # 찾지 못한 경우
    # 왼쪽 밖으로 나간 경우
    if right < 1:
        return 1
    # 오른쪽 밖으로 나간 경우
    elif left > len(dp)-1:
        return len(dp)-1
    # 사이에 있는 경우 -> 차를 구한다.
    else:
        return left

for i in range(N):
    print(dp)
    # dp 맨 마지막에 저장된 원소보다 현재 가리키는 원소가 더 큰 경우 -> dp 리스트 맨 뒤에 원소를 추가한다.
    if dp[len(dp)-1] < A[i]:
        dp.append(A[i])
    # dp 맨 마지막에 저장된 원소가 현재 가리키는 원소보다 작은 경우 -> 인접한 원소 중 큰 값이랑 자리를 바꾼다.
    else:
        dp[findNearest(A[i])] = A[i]

print(dp)
print(len(dp)-1)