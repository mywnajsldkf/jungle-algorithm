from sys import stdin as s

n = int(s.readline())
def move(n, start, finish):
    if(n == 1):
        print(start, finish)
        return

    # 처음 기둥에서 중간 기둥으로 옮긴다.
    move(n-1, start, 6 - start - finish)

    print(start, finish)

    move(n-1, 6 - start - finish, finish)

print(2**n - 1)

if(n <= 20):
    move(n, 1, 3)
