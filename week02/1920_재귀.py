from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
N_Array = list(map(int, s.readline().split()))
M = int(s.readline())
M_Array = list(map(int, s.readline().split()))

def findNumber(array, left, right, key):
    if left > right:
        return "0"

    middle = (left + right) // 2

    if array[middle] == key:
        return "1"
    elif array[middle] < key:
        print("1:", array[middle], key)
        findNumber(array, middle + 1, right, key)
    elif array[middle] > key:
        print("2:",array[middle], key)
        findNumber(array, left, middle - 1, key)


N_Array.sort()

for key in M_Array:
    print(findNumber(N_Array, 0, N-1, key))

