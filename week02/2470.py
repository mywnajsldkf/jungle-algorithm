from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline().rstrip())
liquid = list(map(int, s.readline().rstrip().split(' ')))
liquid.sort()

left, right = 0, N-1

answer = abs(liquid[right] + liquid[left])
final = [liquid[left], liquid[right]]

while left < right:
    left_value = liquid[left]
    right_value = liquid[right]

    total = left_value + right_value
    if abs(total) < answer:
        answer = abs(total)
        final = [left_value, right_value]
        if answer == 0:
            break
    # 양수이면
    if total > 0:
        right -= 1
    # 음수이면
    else:
        left += 1

print(final[0], final[1])