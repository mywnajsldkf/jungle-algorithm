from sys import stdin as s

n = int(s.readline())
def move(n, start, temp, end):
    if(n == 1):
        print(start, end)
        return

    # 처음 기둥에서 중간 기둥으로 옮긴다.
    move(n-1, start, end, temp)

    print(start, end)

    move(n-1, temp, start, end)

print(2**n - 1)

if(n <= 20):
    move(n, 1, 2, 3)