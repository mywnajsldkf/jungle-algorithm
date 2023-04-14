from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline().rstrip())
liquid = list(map(int, s.readline().rstrip().split(' ')))
liquid.sort()

left, right = 0, N-1

answer = abs(liquid[right] + liquid[left])
left_value, right_value = liquid[left], liquid[right]

while left < right:
    total = liquid[left] + liquid[right]

    if abs(total) < answer:
        answer = abs(total)
        left_value = liquid[left]
        right_value = liquid[right]
        if answer == 0:
            break
    # 양수이면
    if total > 0:
        right -= 1
    # 음수이면
    elif total < 0:
        left += 1

print(left_value, right_value)