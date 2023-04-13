from sys import stdin as s

T = int(s.readline())

for i in range(T):
    R, S = s.readline().split()

    P = ""
    S = list(S)

    for j in S:
        P += j*int(R)

    print(P)