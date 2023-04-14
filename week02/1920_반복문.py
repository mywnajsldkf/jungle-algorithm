from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
N_Array = list(map(int, s.readline().split()))
M = int(s.readline())
M_Array = list(map(int, s.readline().split()))

def findNumber(array, key):
    left = 0
    right = N-1

    while True:
        middle = (left + right) // 2
        if array[middle] == key:
            return 1
        elif array[middle] < key:
            left = middle + 1
        else:
            right = middle -1
        if left > right:
            break
    return 0

N_Array.sort()

for key in M_Array:
    print(findNumber(N_Array, key))

