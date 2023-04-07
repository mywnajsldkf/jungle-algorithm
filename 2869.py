from sys import stdin as s

A, B, V = map(int, s.readline().split())

if((V-A) % (A-B) == 0):
    print((V-A)// (A-B)+1)
else:
    print((V-A)//(A-B) + 2)