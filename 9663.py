from sys import stdin as s

N = int(s.readline())
arr = [False]*N
visited = [False]*N

count =0
def nQueen(depth):
    global count
    if(depth == N):
        count += 1
        return

    # 0부터 1까지 바꿔가면서
    for i in range(N):
        if visited[i]:
            continue

        arr[depth] = i
        if(togo(depth)):
            visited[i] = True
            nQueen(depth + 1)
            visited[i] = False

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