from functools import cmp_to_key
from sys import stdin as s

N = int(s.readline())

words = []

for i in range(N):
    word = s.readline().rstrip()
    # 0 -> 단어 / 1 -> 길이

    if [word, len(word)] in words:
        continue
    else:
        words.append([word, len(word)])

def compare(x, y):
    print(words)
    print("x:",x, "y:", y)
    # 단어가 짧은 것이 앞으로
    if(x[1] > y[1]):
        return 1
    # 단어가 짧은 것이 뒤로
    elif(x[1] < y[1]):
        return -1
    # 길이가 같으므로 단어 앞에와 비교
    elif(x[1] == y[1]):
        # 알파벳순으로 정렬 -> 순서 바뀌어야함
        if(x[0] > y[0]):
            return 1
        elif(x[0] < y[0]):
            return -1

result = sorted(words, key=cmp_to_key(compare))

for i in result:
    print(i[0])

'''
n = int(input())
l = []

for _ in range(n):
    l.append(input())

print(l)
l = list(set(l))    # 순서 보장 X
print(l)

l.sort()
print(l)

l.sort(key = len)
print(l)

for i in range(len(l)):
    print(l[i])
'''