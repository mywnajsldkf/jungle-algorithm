from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
A = list(map(int, s.readline().split()))

def lis(arr):
    if len(arr) == 0:
        return 0

    length = 1
    for start in range(len(arr)):
        next = []
        for j in range(start+1, len(arr)):
            if arr[start] < arr[j]:
                next.append(arr[j])
        length = max(length, 1 + lis(next))
    return length

print(lis(A))