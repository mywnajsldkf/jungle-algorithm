from sys import stdin as s

N = int(s.readline())
arr = [False]*N

count = 0
def nQueen(depth):
    global count
    # 다 채워지면
    if(depth == N):
        count += 1
        return

    # 0부터 1까지 바꿔가면서
    for i in range(N):

        arr[depth] = i
        if(togo(depth)):
            nQueen(depth + 1)

def togo(col):
    # 해당 가로까지
    for i in range(col):
        if(arr[i] == arr[col]):
            return False
        elif(abs(col-i) == abs(arr[col] - arr[i])):
            return False

    return True

nQueen(0)
print(count)