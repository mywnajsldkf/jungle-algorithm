from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline().rstrip())
signal = list(map(int, s.readline().rstrip().split()))
stack = []
result = []

for i in range(N):
    while len(stack) > 0:   # stack 이라고만 써도 된다.
        # 맨 뒤에 있는 것이
        if stack[-1][1] > signal[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if len(stack) == 0:     # not stack 이라고 써도 된다.
        result.append(0)
    stack.append([i, signal[i]])

for i in result:
    print(i,end=' ')