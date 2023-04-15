from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
A = list(map(int, s.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if(A[i] > A[j]):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))