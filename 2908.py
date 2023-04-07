from sys import stdin as s

a, b = map(list, s.readline().split())

list_a = list(map(int, a))
list_b = list(map(int, b))

winner = list_a

for i in range(3):
    if(list_a[2-i] > list_b[2-i]):
        winner = list_a
        break
    elif(list_a[2-i] < list_b[2-i]):
        winner = list_b
        break

for i in range(2,-1, -1):
    print(winner[i], end='')