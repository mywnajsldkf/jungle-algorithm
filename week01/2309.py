from sys import stdin as s

nanjang2 = []

for i in range(9):
    nanjang2.append(int(s.readline()))

total = sum(nanjang2)

nanjang2.sort()

now_1 = 0
now_2 = 0

for i in range(8):
    for j in range(i+1, 9):
        if (total - nanjang2[i] - nanjang2[j]) == 100:
            now_1, now_2 = nanjang2[i], nanjang2[j]
            # nanjang2.remove(nanjang2[i])    # 만약 이렇게 빼버리면! 개수가 달라져서 list index out of range 오류가 나온다.
            # nanjang2.remove(nanjang2[j])
            break

nanjang2.remove(now_1)
nanjang2.remove(now_2)

for i in nanjang2:
    print(i)