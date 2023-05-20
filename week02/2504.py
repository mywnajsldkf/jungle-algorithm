from sys import stdin as s

s = open("input.txt", "rt")

line = s.readline()

stack = []
answer = 0
tmp = 1

for i in range(len(line)):
    if line[i] == "(":
        tmp *= 2
        stack.append(line[i])
    elif line[i] == "[":
        tmp *= 3
        stack.append(line[i])
    elif line[i] == ")":
        # stack에 원소가 없거나, 마지막 원소가 [ 라면 -> 종료
        if not stack or stack[-1] == "[":
            answer = 0
            break

        if line[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    elif line[i] == "]":
        # stack에 원소가 없거나, 마지막 원소가 ( 라면 -> 종료
        if not stack or stack[-1] == "(":
            answer = 0
            break

        if line[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)