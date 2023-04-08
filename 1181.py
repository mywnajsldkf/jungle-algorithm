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

words.sort()

def compare(x, y):
    # 단어가 짧은 것이 앞으로
    if(x[1] > y[1]):
        return 1
    elif(x[1] < y[1]):
        return -1
    # 길이가 같으므로 단어 앞에와 비교
    elif(x[1] == y[1]):
        # 알파벳순으로 정렬 -> 순서 바뀌어야함
        if(x[0] > y[0]):
            return 1
        elif(x[0] < y[0]):
            return -1
        else:
            return 0

result = sorted(words, key=cmp_to_key(compare))

for i in result:
    print(i[0])